from pathlib import Path

out_path = Path('.')
index_of_hashes_out_path = out_path / 'hashes'

# Exclude Windows 10 versions for which no ARM64 updates are available.
windows_versions_unsupported = {'1507', '1511', '1607', '1703'}

updates_unsupported = {
    # Temporarily skip an update which returns 404.
    'KB4537762',
    # Temporarily skip an update which returns "The website has encountered a problem", "Error number: 8DDD0024".
    'KB5012643',
}

updates_architecture = 'ARM64'

verbose_run = False
verbose_progress = True
extract_in_a_new_thread = False
exit_on_first_error = True
high_mem_usage_for_performance = False
compression_level = 3

delta_machine_type_values_supported = {
    'CLI4_I386',
    'CLI4_AMD64',
    'CLI4_ARM',
    'CLI4_ARM64',
}

# Non-PE files (very rare).
file_hashes_non_pe = {
    'af700c04f4334cdf9fc575727a055a30855e1ab6a8a480ab6335e1b4a7585173',  # tapi.dll
}
