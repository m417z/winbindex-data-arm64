import json
import argparse

import config
import orjson
from isal import igzip as gzip


def write_to_gzip_file(file, data):
    with open(file, 'wb') as fd:
        with gzip.GzipFile(fileobj=fd, mode='w', compresslevel=config.compression_level, filename='', mtime=0) as gz:
            gz.write(data)


def update_updateinfo_in_files(output_file=None):
    """
    Read updates.json and update the updateInfo entries in all files
    in the by_filename_compressed folder.
    
    Args:
        output_file: Optional path to write the update summary to
    """
    # Read updates.json
    updates_path = config.out_path.joinpath('updates.json')
    if not updates_path.is_file():
        raise RuntimeError(f'{updates_path} not found')

    print(f'Reading {updates_path}...')
    with open(updates_path) as f:
        updates = json.load(f)

    # Create a lookup dictionary for quick access
    # Structure: {windows_version: {update_kb: update_info}}
    updates_lookup = {}
    for windows_version in updates:
        updates_lookup[windows_version] = {}
        for update_kb in updates[windows_version]:
            update_info = updates[windows_version][update_kb]
            updates_lookup[windows_version][update_kb] = update_info

            # Add to other Windows versions if specified
            for other_version in update_info.get('otherWindowsVersions', []):
                if other_version not in updates_lookup:
                    updates_lookup[other_version] = {}
                
                # Check for conflicts - same KB in other version with different data
                if update_kb in updates_lookup[other_version]:
                    if updates_lookup[other_version][update_kb] != update_info:
                        raise RuntimeError(
                            f'Conflicting data for {update_kb} in {other_version}: '
                            f'already exists with different data'
                        )
                else:
                    updates_lookup[other_version][update_kb] = update_info

    print(f'Loaded {sum(len(v) for v in updates_lookup.values())} updates across {len(updates_lookup)} Windows versions')

    # Process files in by_filename_compressed folder
    compressed_dir = config.out_path.joinpath('by_filename_compressed')
    if not compressed_dir.is_dir():
        raise RuntimeError(f'{compressed_dir} not found')

    files_processed = 0
    files_modified = 0
    update_log = set()

    print(f'Processing files in {compressed_dir}...')

    for file_path in sorted(compressed_dir.glob('*.json.gz')):
        files_processed += 1

        if files_processed % 1000 == 0:
            print(f'Processed {files_processed} files...')

        # Read the compressed file
        with gzip.open(file_path, 'rb') as f:
            data = orjson.loads(f.read())

        # Track if any changes were made
        file_modified = False

        # Iterate through all file hashes in this file
        for file_hash, file_data in data.items():
            if 'windowsVersions' not in file_data:
                raise RuntimeError(f'{file_path.stem} missing windowsVersions for hash {file_hash}')

            # Iterate through windows versions
            for windows_version, version_data in file_data['windowsVersions'].items():
                if windows_version not in updates_lookup:
                    raise RuntimeError(f'{file_path.stem} contains unknown Windows version {windows_version}')

                # Iterate through update KBs
                for update_kb, kb_data in version_data.items():
                    # Skip BASE entries (from ISO files)
                    if update_kb == 'BASE':
                        continue

                    # Check if this update_kb exists in updates.json
                    if update_kb not in updates_lookup[windows_version]:
                        raise RuntimeError(f'{file_path.stem} contains update_kb {update_kb} for {windows_version} which is not in updates.json')

                    # Update the updateInfo
                    new_update_info = updates_lookup[windows_version][update_kb]

                    if 'updateInfo' not in kb_data:
                        raise RuntimeError(f'{file_path.stem} missing updateInfo for {update_kb} on {windows_version}')

                    old_update_info = kb_data['updateInfo']
                    if old_update_info != new_update_info:
                        # Find only the keys that changed
                        all_keys = set(old_update_info.keys()) | set(new_update_info.keys())
                        changed_keys = {k for k in all_keys if old_update_info.get(k) != new_update_info.get(k)}

                        if changed_keys:
                            old_diff = {k: old_update_info[k] for k in changed_keys if k in old_update_info}
                            new_diff = {k: new_update_info[k] for k in changed_keys if k in new_update_info}
                            update_log.add((
                                json.dumps(old_diff, sort_keys=True),
                                json.dumps(new_diff, sort_keys=True),
                            ))

                        kb_data['updateInfo'] = new_update_info
                        file_modified = True

        # Write back if modified
        if file_modified:
            files_modified += 1
            write_to_gzip_file(file_path, orjson.dumps(data))

    print(f'Files processed: {files_processed}')
    print(f'Files modified: {files_modified}')

    # Print to console
    for old_info, new_info in sorted(update_log):
        print()
        print(old_info)
        print('->')
        print(new_info)

    # Write to file if requested
    if output_file and update_log:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('Updated updateInfo as following:\n')
            for old_info, new_info in sorted(update_log):
                f.write('\n')
                f.write(old_info + '\n')
                f.write('->\n')
                f.write(new_info + '\n')
        print(f'Summary written to {output_file}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update updateInfo entries in by_filename_compressed files')
    parser.add_argument('--output', '-o', type=str, help='Output file for update summary')
    args = parser.parse_args()

    update_updateinfo_in_files(output_file=args.output)
