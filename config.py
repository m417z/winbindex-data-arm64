from pathlib import Path

out_path_override = Path('.out_path_override')
out_path = Path(out_path_override.read_text().strip() if out_path_override.exists() else '.')
index_of_hashes_title = 'Winbindex ARM64 Hashes'
index_of_hashes_out_path = out_path / 'hashes'

deploy_save_disk_space = True
deploy_amend_last_commit = True

# Exclude Windows versions for which no ARM64 updates are available from a specific date.
windows_versions_unsupported = {
    '1507': None,
    '1511': None,
    '1607': None,
    '1703': None,
    '1809': '2024-07-09',
}

updates_unsupported = {
    # Temporarily skip an update which returns "The website has encountered a problem", "Error number: 8DDD0024".
    'KB5012643',
}

updates_architecture = 'ARM64'
updates_never_removed = True
allow_missing_sha256_hash = False
allow_unknown_non_pe_files = False

verbose_run = False
verbose_progress = True
extract_in_a_new_thread = False
exit_on_first_error = True
high_mem_usage_for_performance = False
compression_level = 3
group_by_filename_processes = 4

delta_machine_type_values_supported = {
    'CLI4_I386',
    'CLI4_AMD64',
    'CLI4_ARM',
    'CLI4_ARM64',
}

delta_data_without_rift_table_names = {
    '*.mui',
    'powershell_ise.exe',
}
delta_data_without_rift_table_manifests = {
    'arm64_microsoft-nxt-boottocloud-windows365-app_*',
}

# Non-PE files (very rare).
file_hashes_non_pe = {
    'af700c04f4334cdf9fc575727a055a30855e1ab6a8a480ab6335e1b4a7585173',  # tapi.dll
}

tcb_launcher_descriptions = ['TCB Launcher']
tcb_launcher_large_first_section_virtual_addresses = [0x1000, 0x3000, 0x4000, 0x6000]

file_hashes_unusual_section_alignment = {
    'ede86c8d8c6b9256b926701f4762bd6f71e487f366dfc7db8d74b8af57e79bbb': {'first_section_virtual_address': 0x380, 'section_alignment': 0x80},  # ftdibus.sys
    '5bec55192eaef43b0fade13bbadfdf77eb0d45b4b281ae19d4b0b7a0c2350836': {'first_section_virtual_address': 0x2d0, 'section_alignment': 0x10},  # onnxruntime.dll
    '09ced31cad8547a9ee5dcf739565def2f4359075e56a7b699cc85971e0905864': {'first_section_virtual_address': 0x310, 'section_alignment': 0x10},  # onnxruntime.dll
}

file_hashes_zero_timestamp = {
    '18dd945c04ce0fbe882cd3f234c2da2d0faa12b23bd6df7b1edc31faecf51c69',  # brlapi-0.8.dll
    '7a9113d00a274c075c58b22a3ebacf1754e7da7cfb4d3334b90367b602158d78',  # brltty.exe
}

file_hashes_small_non_signature_overlay = {
    '11efef27aea856060bdeb6d2f0d62c68088eb891997d4e99de708a6b51743148',  # brlapi-0.6.dll
    'b175123eff88d1573f451b286cd5370003a0839e53c7ae86bf22b35b7e77bad3',  # brlapi-0.6.dll
    '18dd945c04ce0fbe882cd3f234c2da2d0faa12b23bd6df7b1edc31faecf51c69',  # brlapi-0.8.dll
    '3eaa62334520b41355c5103dcd663744ba26caae3496bd9015bc399fbaf42fce',  # brltty.exe
    '69f83db2fda7545ab0a1c60056aee472bf3c70a0af7454c51e1cd449b5c7f43b',  # brltty.exe
    '7a9113d00a274c075c58b22a3ebacf1754e7da7cfb4d3334b90367b602158d78',  # brltty.exe
    'b4cc93cf4d7c2906c1929c079cd98ef00c7a33832e132ac57adde71857082e36',  # libgcc_s_dw2-1.dll
}

file_hashes_unsigned_with_overlay = {
    'cf54a8504f2dbdd7bea3acdcd065608d21f5c06924baf647955cc28b8637ae68',  # libiconv-2.dll
    'ee1df918ca67581f21eac49ae4baffca959f71d1a0676d7c35bc5fb96bea3a48',  # libiconv-2.dll
    '9eec7e5188d1a224325281e4d0e6e1d5f9f034f02bd1fadeb792d3612c72319e',  # libpdcurses.dll
    'f9b385e19b9d57a1d1831e744ed2d1c3bb8396d28f48d10120cecfe72595b222',  # libpdcursesu.dll
    '787d5c07ab0bb782dede7564840e86c468e3728e81266dae23eb8ad614bcee95',  # libpdcursesw.dll
}

file_details_unsigned_with_overlay = []

# Details: https://gist.github.com/m417z/3248c18efd942f63013b8d3035e2dc79
file_hashes_mismatch = {
    # wfascim_uninstall.mof in KB5025298 and newer Windows 11 21H2 updates.
    ('cee501be4532071c6fe1df2933d98f8fccba4803de481746808386c3245ad6a7', '9e51833f306f8c5c59bc8f041a9ec1bb'): {'11-21H2'},
}
