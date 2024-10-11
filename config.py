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

updates_unsupported = set()

# updates_alternative_links = {
#     # The update server returns "The website has encountered a problem", "Error number: 8DDD0024".
#     ('11-21H2', 'KB5012643'): 'https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/updt/2022/04/windows10.0-kb5012643-arm64_26ae3882c036a817235c8e9be57407dae7f957ec.msu',
#     # The update server returns "The update requested could not be found", "Error number: 8DDD0024".
#     ('20H2', 'KB5018410'): 'https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2022/10/windows10.0-kb5018410-arm64_a0d4c6caf83af34442728052eb3e1002add312fb.msu',
# }
updates_alternative_links={}
updates_alternative_links["1709"]={}
updates_alternative_links["1709"]["KB4043961"]={}
updates_alternative_links["1709"]["KB4043961"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2017/10/windows10.0-kb4043961-arm64_a48d09f78669648b42444c64c1d426a556c6039a.msu"
updates_alternative_links["1709"]["KB4048955"]={}
updates_alternative_links["1709"]["KB4051963"]={}
updates_alternative_links["1709"]["KB4052314"]={}
updates_alternative_links["1709"]["KB4054517"]={}
updates_alternative_links["1709"]["KB4054517"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2017/12/windows10.0-kb4054517-arm64_eddf4992fd8d7c000a6411e43e5dae7309588327.msu"
updates_alternative_links["1709"]["KB4056342"]={}
updates_alternative_links["1709"]["KB4056892"]={}
updates_alternative_links["1709"]["KB4056892"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2018/01/windows10.0-kb4056892-arm64_028810421e6036f439add546e189219649140f4b.msu"
updates_alternative_links["1709"]["KB4058258"]={}
updates_alternative_links["1709"]["KB4073117"]={}
updates_alternative_links["1709"]["KB4073290"]={}
updates_alternative_links["1709"]["KB4073291"]={}
updates_alternative_links["1709"]["KB4074588"]={}
updates_alternative_links["1709"]["KB4074588"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2018/02/windows10.0-kb4074588-arm64_ab51bdbab9d9ba454c6917cf5779e27ede2c358e.msu"
updates_alternative_links["1709"]["KB4077675"]={}
updates_alternative_links["1709"]["KB4088776"]={}
updates_alternative_links["1709"]["KB4088776"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2018/03/windows10.0-kb4088776-arm64_8f0e45eb4d1e861e9002b5216c21eece8d1361d3.msu"
updates_alternative_links["1709"]["KB4512516"]={}
updates_alternative_links["1709"]["KB4512516"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2019/08/windows10.0-kb4512516-arm64_f78029ee85ac86e3d85d4b56b11051e08eb795bc.msu"
updates_alternative_links["1709"]["KB4513172"]={}
updates_alternative_links["1709"]["KB4516066"]={}
updates_alternative_links["1709"]["KB4516066"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/09/windows10.0-kb4516066-arm64_3b7288cb014c80b451387ec971583354e3a5d840.msu"
updates_alternative_links["1709"]["KB4516071"]={}
updates_alternative_links["1709"]["KB4516071"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/updt/2019/09/windows10.0-kb4516071-arm64_b0e40c1ae7b96057e4057252abda59cf267d3e69.msu"
updates_alternative_links["1709"]["KB4518514"]={}
updates_alternative_links["1709"]["KB4520004"]={}
updates_alternative_links["1709"]["KB4520004"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/10/windows10.0-kb4520004-arm64_742fedb71ea1ef6a804126bab724535ac3272a50.msu"
updates_alternative_links["1709"]["KB4520006"]={}
updates_alternative_links["1709"]["KB4522012"]={}
updates_alternative_links["1709"]["KB4522809"]={}
updates_alternative_links["1709"]["KB4522811"]={}
updates_alternative_links["1709"]["KB4522812"]={}
updates_alternative_links["1709"]["KB4524150"]={}
updates_alternative_links["1709"]["KB4524150"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/09/windows10.0-kb4524150-arm64_d3732d3d242310f17dc288e3049d8c6b20214acd.msu"
updates_alternative_links["1803"]={}
updates_alternative_links["1803"]["KB4100403"]={}
updates_alternative_links["1803"]["KB4103721"]={}
updates_alternative_links["1803"]["KB4103721"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2018/05/windows10.0-kb4103721-arm64_bea8bfddecb0465f3368cd99b1c1b3663a2109a3.msu"
updates_alternative_links["1803"]["KB4467682"]={}
updates_alternative_links["1803"]["KB4467682"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/updt/2018/11/windows10.0-kb4467682-arm64_54ddf19a90e7d694a25f95e4c8ef9b07028e9bd4.msu"
updates_alternative_links["1803"]["KB4516058"]={}
updates_alternative_links["1803"]["KB4516058"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2019/09/windows10.0-kb4516058-arm64_b64f03517861c3b9e2b6b045aa4a5e9729e2e789.msu"
updates_alternative_links["1803"]["KB4519978"]={}
updates_alternative_links["1803"]["KB4520008"]={}
updates_alternative_links["1803"]["KB4520008"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/10/windows10.0-kb4520008-arm64_85cb7562c7873b86a8fdb0c18a3bcb81e43bcb34.msu"
updates_alternative_links["1803"]["KB4522014"]={}
updates_alternative_links["1803"]["KB4522014"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2019/09/windows10.0-kb4522014-arm64_d268ac9db40d9458f2ab05801ca491ed6af0229a.msu"
updates_alternative_links["1803"]["KB4524149"]={}
updates_alternative_links["1803"]["KB4524149"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/09/windows10.0-kb4524149-arm64_1da9f1ce80d03ea63603095649ae765a40f030b2.msu"
updates_alternative_links["1803"]["KB4525237"]={}
updates_alternative_links["1803"]["KB4525237"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/11/windows10.0-kb4525237-arm64_0b934ac3d6f6acc0fcad7f3b66850324c99e062b.msu"
updates_alternative_links["1803"]["KB4530717"]={}
updates_alternative_links["1803"]["KB4530717"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/12/windows10.0-kb4530717-arm64_132fe6b45e75e44ec6ddaf8f00575645b39fff7c.msu"
updates_alternative_links["1803"]["KB4534293"]={}
updates_alternative_links["1803"]["KB4534308"]={}
updates_alternative_links["1803"]["KB4537762"]={}
updates_alternative_links["1803"]["KB4537795"]={}
updates_alternative_links["1803"]["KB4540689"]={}
updates_alternative_links["1803"]["KB4541333"]={}
updates_alternative_links["1803"]["KB4550922"]={}
updates_alternative_links["1803"]["KB4550944"]={}
updates_alternative_links["1803"]["KB4554349"]={}
updates_alternative_links["1803"]["KB4556807"]={}
updates_alternative_links["1803"]["KB4561621"]={}
updates_alternative_links["1803"]["KB4565489"]={}
updates_alternative_links["1803"]["KB4567514"]={}
updates_alternative_links["1803"]["KB4571709"]={}
updates_alternative_links["1803"]["KB4571709"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2020/08/windows10.0-kb4571709-arm64_ad80e40f871d70fe27f883fb3709d71d4f44889f.msu"
updates_alternative_links["1803"]["KB4577032"]={}
updates_alternative_links["1803"]["KB4577032"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/09/windows10.0-kb4577032-arm64_f416eaf6a369ec952a1174d69b40f978756f3688.msu"
updates_alternative_links["1803"]["KB4580330"]={}
updates_alternative_links["1803"]["KB4580330"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/10/windows10.0-kb4580330-arm64_b07ad4439c912cf2840e9bce6361495f7543e1b4.msu"
updates_alternative_links["1803"]["KB4586785"]={}
updates_alternative_links["1803"]["KB4586785"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2020/11/windows10.0-kb4586785-arm64_fe5367f8a1d7ff5efb845ef7e479eb0c72fccf11.msu"
updates_alternative_links["1803"]["KB4592446"]={}
updates_alternative_links["1803"]["KB4592446"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2020/12/windows10.0-kb4592446-arm64_a331fd969a7ae7580fcbda99613e324f609d3ce2.msu"
updates_alternative_links["1803"]["KB4598245"]={}
updates_alternative_links["1803"]["KB4598245"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/01/windows10.0-kb4598245-arm64_388f9378922d3c3a4740905b412e9ee948978ce8.msu"
updates_alternative_links["1803"]["KB4601354"]={}
updates_alternative_links["1803"]["KB4601354"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/02/windows10.0-kb4601354-arm64_20f0456cb4f5484ec5e9d71d47409912cf004417.msu"
updates_alternative_links["1803"]["KB5000809"]={}
updates_alternative_links["1803"]["KB5001339"]={}
updates_alternative_links["1803"]["KB5001565"]={}
updates_alternative_links["1803"]["KB5001634"]={}
updates_alternative_links["1803"]["KB5003174"]={}
updates_alternative_links["1809"]={}
updates_alternative_links["1809"]["KB4464330"]={}
updates_alternative_links["1809"]["KB4464330"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2018/10/windows10.0-kb4464330-arm64_c493fb68d917f29fa11ed444571c35d5759b3eb7.msu"
updates_alternative_links["1809"]["KB4464455"]={}
updates_alternative_links["1809"]["KB4467708"]={}
updates_alternative_links["1809"]["KB4467708"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2018/11/windows10.0-kb4467708-arm64_e44e7c3c49bc0d3cb6bc45b87a561a48b59e1457.msu"
updates_alternative_links["1809"]["KB4469342"]={}
updates_alternative_links["1809"]["KB4471332"]={}
updates_alternative_links["1809"]["KB4471332"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2018/12/windows10.0-kb4471332-arm64_d7f92de84bdc7558c7b9408646b0f0fd533d0a26.msu"
updates_alternative_links["1809"]["KB4476976"]={}
updates_alternative_links["1809"]["KB4480116"]={}
updates_alternative_links["1809"]["KB4480116"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2019/01/windows10.0-kb4480116-arm64_bacbad707cce6698fde3ffbb1daca2f555009e08.msu"
updates_alternative_links["1809"]["KB4482887"]={}
updates_alternative_links["1809"]["KB4483235"]={}
updates_alternative_links["1809"]["KB4483235"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2018/12/windows10.0-kb4483235-arm64_f2375c94f1bd67092a35c0f867b50f8a4f44f914.msu"
updates_alternative_links["1809"]["KB4487044"]={}
updates_alternative_links["1809"]["KB4487044"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2019/02/windows10.0-kb4487044-arm64_4d0043b098cb0d5efcd6fc4eb250e60c6697c215.msu"
updates_alternative_links["1809"]["KB4489899"]={}
updates_alternative_links["1809"]["KB4489899"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/03/windows10.0-kb4489899-arm64_8f09a69bb87fa967268adeb08b564b5f75438478.msu"
updates_alternative_links["1809"]["KB4490481"]={}
updates_alternative_links["1809"]["KB4493509"]={}
updates_alternative_links["1809"]["KB4493509"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/04/windows10.0-kb4493509-arm64_d490c6db66de97ad9f215898b7606fd5408ac8b1.msu"
updates_alternative_links["1809"]["KB4494441"]={}
updates_alternative_links["1809"]["KB4494441"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2019/05/windows10.0-kb4494441-arm64_edda2c6414f1d99eef66a3c54b3ac54883e1c0f4.msu"
updates_alternative_links["1809"]["KB4495667"]={}
updates_alternative_links["1809"]["KB4497934"]={}
updates_alternative_links["1809"]["KB4501371"]={}
updates_alternative_links["1809"]["KB4501835"]={}
updates_alternative_links["1809"]["KB4503327"]={}
updates_alternative_links["1809"]["KB4503327"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2019/06/windows10.0-kb4503327-arm64_9cc6e7b5060de49b29b388f2c8d81e529bc06565.msu"
updates_alternative_links["1809"]["KB4505056"]={}
updates_alternative_links["1809"]["KB4505658"]={}
updates_alternative_links["1809"]["KB4507469"]={}
updates_alternative_links["1809"]["KB4507469"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/07/windows10.0-kb4507469-arm64_e46308e09e04da3cb7276787071fd100880ab87d.msu"
updates_alternative_links["1809"]["KB4509479"]={}
updates_alternative_links["1809"]["KB4511553"]={}
updates_alternative_links["1809"]["KB4511553"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/08/windows10.0-kb4511553-arm64_4feacf773bc63cbc573dba4de6b38471c222d469.msu"
updates_alternative_links["1809"]["KB4512534"]={}
updates_alternative_links["1809"]["KB4512578"]={}
updates_alternative_links["1809"]["KB4512578"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2019/09/windows10.0-kb4512578-arm64_7fd53c2bd1a847096abdfc96bc0dcbdc20e63fc8.msu"
updates_alternative_links["1809"]["KB4516077"]={}
updates_alternative_links["1809"]["KB4516077"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/updt/2019/09/windows10.0-kb4516077-arm64_75ded62a08f3366f4d36b833a0e6b59ee8b9c691.msu"
updates_alternative_links["1809"]["KB4519338"]={}
updates_alternative_links["1809"]["KB4519338"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2019/10/windows10.0-kb4519338-arm64_9fadab01ccc013e84ef1827bd65d84ad0c336966.msu"
updates_alternative_links["1809"]["KB4520062"]={}
updates_alternative_links["1809"]["KB4522015"]={}
updates_alternative_links["1809"]["KB4522015"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/09/windows10.0-kb4522015-arm64_2d5ed3c38c2f88832097de03e32ee490e8eece6a.msu"
updates_alternative_links["1809"]["KB4523205"]={}
updates_alternative_links["1809"]["KB4523205"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/11/windows10.0-kb4523205-arm64_f49f0ec522a536537e8a10f569f78d0c2a8de017.msu"
updates_alternative_links["1809"]["KB4524148"]={}
updates_alternative_links["1809"]["KB4524148"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/09/windows10.0-kb4524148-arm64_1c6016b4b5927190e0932326e05f3751a3efc7b0.msu"
updates_alternative_links["1809"]["KB4530715"]={}
updates_alternative_links["1809"]["KB4530715"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2019/12/windows10.0-kb4530715-arm64_af99d8fae73cfead913f20ac95e99d4d181a4f91.msu"
updates_alternative_links["1809"]["KB4532691"]={}
updates_alternative_links["1809"]["KB4532691"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/02/windows10.0-kb4532691-arm64_d8175151a67618db5ba20306ab1a3aca1ea15a76.msu"
updates_alternative_links["1809"]["KB4534273"]={}
updates_alternative_links["1809"]["KB4534273"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/01/windows10.0-kb4534273-arm64_40e88329f5a2de640841b3ddd5222d7d1f835a00.msu"
updates_alternative_links["1809"]["KB4534321"]={}
updates_alternative_links["1809"]["KB4534321"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/updt/2020/01/windows10.0-kb4534321-arm64_c9dadd923e2aedd3096b99e0b4c62acfbf227703.msu"
updates_alternative_links["1809"]["KB4537818"]={}
updates_alternative_links["1809"]["KB4538461"]={}
updates_alternative_links["1809"]["KB4538461"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2020/03/windows10.0-kb4538461-arm64_4b9cd3e4eecee7ecfbf7f9db9be9a59d7007be66.msu"
updates_alternative_links["1809"]["KB4541331"]={}
updates_alternative_links["1809"]["KB4549949"]={}
updates_alternative_links["1809"]["KB4549949"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/04/windows10.0-kb4549949-arm64_f8a7a20d6a30a37f8c0dd679c988afb5402e7801.msu"
updates_alternative_links["1809"]["KB4550969"]={}
updates_alternative_links["1809"]["KB4551853"]={}
updates_alternative_links["1809"]["KB4551853"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2020/05/windows10.0-kb4551853-arm64_079ef5c627153dd4a58af0e7a83715a0d89d5704.msu"
updates_alternative_links["1809"]["KB4554354"]={}
updates_alternative_links["1809"]["KB4558998"]={}
updates_alternative_links["1809"]["KB4558998"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/07/windows10.0-kb4558998-arm64_1e2068abdabb80265526992a5dbe467af943f0b3.msu"
updates_alternative_links["1809"]["KB4559003"]={}
updates_alternative_links["1809"]["KB4561608"]={}
updates_alternative_links["1809"]["KB4561608"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2020/06/windows10.0-kb4561608-arm64_bd0d3957bc71f8c55638ddbf0735c94a1d901ed7.msu"
updates_alternative_links["1809"]["KB4565349"]={}
updates_alternative_links["1809"]["KB4565349"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/08/windows10.0-kb4565349-arm64_f6ba88d20aabfd1ba661c1d83dd46e54422b6e5d.msu"
updates_alternative_links["1809"]["KB4567513"]={}
updates_alternative_links["1809"]["KB4570333"]={}
updates_alternative_links["1809"]["KB4570333"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/09/windows10.0-kb4570333-arm64_c3de5972054093883bb46eeea675b7d5b96777c9.msu"
updates_alternative_links["1809"]["KB4571748"]={}
updates_alternative_links["1809"]["KB4577069"]={}
updates_alternative_links["1809"]["KB4577668"]={}
updates_alternative_links["1809"]["KB4577668"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2020/10/windows10.0-kb4577668-arm64_b75ce1f8ce6333205582be3f3a029e73ef123e83.msu"
updates_alternative_links["1809"]["KB4580390"]={}
updates_alternative_links["1809"]["KB4586793"]={}
updates_alternative_links["1809"]["KB4586793"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2020/11/windows10.0-kb4586793-arm64_fd71c9aaf4dd0f25e53e36d515bbbbf00e174486.msu"
updates_alternative_links["1809"]["KB4586839"]={}
updates_alternative_links["1809"]["KB4592440"]={}
updates_alternative_links["1809"]["KB4592440"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/12/windows10.0-kb4592440-arm64_005ed3b662c4b64e00d1a5000157a5eeee610b2f.msu"
updates_alternative_links["1809"]["KB4594442"]={}
updates_alternative_links["1809"]["KB4598230"]={}
updates_alternative_links["1809"]["KB4598230"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/01/windows10.0-kb4598230-arm64_67fb195ee9ba5742f42b39610118224a7439c673.msu"
updates_alternative_links["1809"]["KB4598296"]={}
updates_alternative_links["1809"]["KB4601345"]={}
updates_alternative_links["1809"]["KB4601345"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/02/windows10.0-kb4601345-arm64_e1a455d6b5a3359d50d92393f7be6ea12a8c4865.msu"
updates_alternative_links["1809"]["KB4601383"]={}
updates_alternative_links["1809"]["KB5000822"]={}
updates_alternative_links["1809"]["KB5000822"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/03/windows10.0-kb5000822-arm64_94bdd8899dbd27ef4e22f3973e47995b18702ad0.msu"
updates_alternative_links["1809"]["KB5000854"]={}
updates_alternative_links["1809"]["KB5001342"]={}
updates_alternative_links["1809"]["KB5001342"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/04/windows10.0-kb5001342-arm64_a08a51f259643c83e4b8119eb884c338f7b1b61e.msu"
updates_alternative_links["1809"]["KB5001384"]={}
updates_alternative_links["1809"]["KB5001568"]={}
updates_alternative_links["1809"]["KB5001638"]={}
updates_alternative_links["1809"]["KB5003171"]={}
updates_alternative_links["1809"]["KB5003217"]={}
updates_alternative_links["1809"]["KB5003646"]={}
updates_alternative_links["1809"]["KB5003646"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/06/windows10.0-kb5003646-arm64_7487bac07c65ec9f651d2643a3c6ade18b34b0d8.msu"
updates_alternative_links["1809"]["KB5003703"]={}
updates_alternative_links["1809"]["KB5004244"]={}
updates_alternative_links["1809"]["KB5004244"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/07/windows10.0-kb5004244-arm64_d167688dfc6314004431a6008218e92e9339dda6.msu"
updates_alternative_links["1809"]["KB5004308"]={}
updates_alternative_links["1809"]["KB5004947"]={}
updates_alternative_links["1809"]["KB5004947"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/07/windows10.0-kb5004947-arm64_e7b17898d727a06cdabb34036fea645cbed3b243.msu"
updates_alternative_links["1809"]["KB5005030"]={}
updates_alternative_links["1809"]["KB5005030"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/08/windows10.0-kb5005030-arm64_d993932e1840f823051a4af6fb2d370c259f28b3.msu"
updates_alternative_links["1809"]["KB5005102"]={}
updates_alternative_links["1809"]["KB5005394"]={}
updates_alternative_links["1809"]["KB5005568"]={}
updates_alternative_links["1809"]["KB5005568"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/09/windows10.0-kb5005568-arm64_c5d9c67b2b1a54905420460b6a36a48dc7965f7d.msu"
updates_alternative_links["1809"]["KB5005625"]={}
updates_alternative_links["1809"]["KB5006672"]={}
updates_alternative_links["1809"]["KB5006672"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/10/windows10.0-kb5006672-arm64_12c48d5462b54062c4940e879a28aad4c34267e4.msu"
updates_alternative_links["1809"]["KB5006744"]={}
updates_alternative_links["1809"]["KB5007206"]={}
updates_alternative_links["1809"]["KB5007206"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/11/windows10.0-kb5007206-arm64_7885b4728f9c0a69a1f474d41365ece6d28f9490.msu"
updates_alternative_links["1809"]["KB5007266"]={}
updates_alternative_links["1809"]["KB5008218"]={}
updates_alternative_links["1809"]["KB5008218"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/12/windows10.0-kb5008218-arm64_053b486d47955ffedbc356f5edbb429008d3b482.msu"
updates_alternative_links["1809"]["KB5008602"]={}
updates_alternative_links["1809"]["KB5009557"]={}
updates_alternative_links["1809"]["KB5009557"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2022/01/windows10.0-kb5009557-arm64_08a1a497852d5e3f95f426f5db177b4da9e657e5.msu"
updates_alternative_links["1809"]["KB5009616"]={}
updates_alternative_links["1809"]["KB5010196"]={}
updates_alternative_links["1809"]["KB5010351"]={}
updates_alternative_links["1809"]["KB5010351"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2022/02/windows10.0-kb5010351-arm64_f978dc623fb68c80ce9d49c775f593e6ec1412aa.msu"
updates_alternative_links["1809"]["KB5010427"]={}
updates_alternative_links["1809"]["KB5010791"]={}
updates_alternative_links["1809"]["KB5011503"]={}
updates_alternative_links["1809"]["KB5011503"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2022/03/windows10.0-kb5011503-arm64_beec3d7f5bad0a7fdeefc7987807c7087b51ebc5.msu"
updates_alternative_links["1809"]["KB5011551"]={}
updates_alternative_links["1809"]["KB5012636"]={}
updates_alternative_links["1809"]["KB5012647"]={}
updates_alternative_links["1809"]["KB5012647"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2022/04/windows10.0-kb5012647-arm64_80479c0badc037466e8415042d5c8fc545b3de9a.msu"
updates_alternative_links["1809"]["KB5013941"]={}
updates_alternative_links["1809"]["KB5013941"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2022/05/windows10.0-kb5013941-arm64_35f4da284caa85cfaa8a900340bf36748c83dba2.msu"
updates_alternative_links["1809"]["KB5014022"]={}
updates_alternative_links["1809"]["KB5014669"]={}
updates_alternative_links["1809"]["KB5014692"]={}
updates_alternative_links["1809"]["KB5014692"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2022/06/windows10.0-kb5014692-arm64_1a5efc016d638d0701a84d93079ac14266c31704.msu"
updates_alternative_links["1809"]["KB5015018"]={}
updates_alternative_links["1809"]["KB5015811"]={}
updates_alternative_links["1809"]["KB5015811"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2022/07/windows10.0-kb5015811-arm64_f846d820dbd2f9c3e42148cbbb78b4a77986fd3a.msu"
updates_alternative_links["1809"]["KB5015880"]={}
updates_alternative_links["1809"]["KB5016623"]={}
updates_alternative_links["1809"]["KB5016623"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2022/08/windows10.0-kb5016623-arm64_9cc3b4c3db796bcb7fe01167c9f6d93fd41da8da.msu"
updates_alternative_links["1903"]={}
updates_alternative_links["1903"]["KB4497935"]={}
updates_alternative_links["1903"]["KB4501375"]={}
updates_alternative_links["1903"]["KB4503293"]={}
updates_alternative_links["1903"]["KB4503293"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2019/06/windows10.0-kb4503293-arm64_ffd3fb7c0d325004829b63349f4471962479e198.msu"
updates_alternative_links["1903"]["KB4505057"]={}
updates_alternative_links["1903"]["KB4505903"]={}
updates_alternative_links["1903"]["KB4507453"]={}
updates_alternative_links["1903"]["KB4507453"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2019/07/windows10.0-kb4507453-arm64_208bce1e83ff4941d78025aafb2f119945dc5b13.msu"
updates_alternative_links["1903"]["KB4512508"]={}
updates_alternative_links["1903"]["KB4512508"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2019/08/windows10.0-kb4512508-arm64_7bdf8ac4c16e78892aaa5370451d36db0bab8cd2.msu"
updates_alternative_links["1903"]["KB4512941"]={}
updates_alternative_links["1903"]["KB4515384"]={}
updates_alternative_links["1903"]["KB4515384"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2019/09/windows10.0-kb4515384-arm64_6480ee5b66e51fc3e2d67e70fb9c27ed94ebb460.msu"
updates_alternative_links["1903"]["KB4517211"]={}
updates_alternative_links["1903"]["KB4517389"]={}
updates_alternative_links["1903"]["KB4522016"]={}
updates_alternative_links["1903"]["KB4522016"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/09/windows10.0-kb4522016-arm64_a87772302136f33858f278130959aa182ed783b5.msu"
updates_alternative_links["1903"]["KB4522355"]={}
updates_alternative_links["1903"]["KB4524147"]={}
updates_alternative_links["1903"]["KB4524147"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/10/windows10.0-kb4524147-arm64_cb1ff16424fbd2f200e84fa60572f6c6ba87a2b9.msu"
updates_alternative_links["1903"]["KB4524570"]={}
updates_alternative_links["1903"]["KB4528760"]={}
updates_alternative_links["1903"]["KB4528760"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/01/windows10.0-kb4528760-arm64_63f0d70d98313e642ff2db6d4dd489454cea6b6f.msu"
updates_alternative_links["1903"]["KB4530684"]={}
updates_alternative_links["1903"]["KB4530684"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2019/12/windows10.0-kb4530684-arm64_1c16911fd123e5e5b1abee2913a2c7bba9f55974.msu"
updates_alternative_links["1903"]["KB4532693"]={}
updates_alternative_links["1903"]["KB4532693"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/02/windows10.0-kb4532693-arm64_3d7d8b42ea8a8c9b3c2a529fca160ce28e909342.msu"
updates_alternative_links["1903"]["KB4532695"]={}
updates_alternative_links["1903"]["KB4535996"]={}
updates_alternative_links["1903"]["KB4540673"]={}
updates_alternative_links["1903"]["KB4540673"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2020/03/windows10.0-kb4540673-arm64_26018c78615c940db15fcc9322f79c97d6ab7825.msu"
updates_alternative_links["1903"]["KB4541335"]={}
updates_alternative_links["1903"]["KB4549951"]={}
updates_alternative_links["1903"]["KB4549951"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/04/windows10.0-kb4549951-arm64_aafe314c953d5ac900a6dd7d80bf354c078d2a1a.msu"
updates_alternative_links["1903"]["KB4550945"]={}
updates_alternative_links["1903"]["KB4551762"]={}
updates_alternative_links["1903"]["KB4551762"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2020/03/windows10.0-kb4551762-arm64_d000cc232d2a93161073b3cde47ee9a43b4e412b.msu"
updates_alternative_links["1903"]["KB4554364"]={}
updates_alternative_links["1903"]["KB4556799"]={}
updates_alternative_links["1903"]["KB4556799"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2020/05/windows10.0-kb4556799-arm64_d0fc6fe39bc090e160cd8a074dda73e3cf788e2a.msu"
updates_alternative_links["1903"]["KB4559004"]={}
updates_alternative_links["1903"]["KB4560960"]={}
updates_alternative_links["1903"]["KB4560960"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/06/windows10.0-kb4560960-arm64_88e2847b3c3276795516987768e69a5030981488.msu"
updates_alternative_links["1903"]["KB4565351"]={}
updates_alternative_links["1903"]["KB4565351"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/08/windows10.0-kb4565351-arm64_d51b3e823d3120fcb70162f8a51083bd222b002a.msu"
updates_alternative_links["1903"]["KB4565483"]={}
updates_alternative_links["1903"]["KB4565483"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/07/windows10.0-kb4565483-arm64_b175163474fe04830d22fd76b825c75c62393f74.msu"
updates_alternative_links["1903"]["KB4566116"]={}
updates_alternative_links["1903"]["KB4567512"]={}
updates_alternative_links["1903"]["KB4574727"]={}
updates_alternative_links["1903"]["KB4574727"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/09/windows10.0-kb4574727-arm64_ec7efb576f0ce38fe9f130f065d0b6304d066b8d.msu"
updates_alternative_links["1903"]["KB4577062"]={}
updates_alternative_links["1903"]["KB4577671"]={}
updates_alternative_links["1903"]["KB4580386"]={}
updates_alternative_links["1903"]["KB4586786"]={}
updates_alternative_links["1903"]["KB4586819"]={}
updates_alternative_links["1903"]["KB4592449"]={}
updates_alternative_links["1903"]["KB4594443"]={}
updates_alternative_links["1909"]={}
updates_alternative_links["1909"]["KB4598229"]={}
updates_alternative_links["1909"]["KB4598229"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/01/windows10.0-kb4598229-arm64_1c5e24b213ab8dc7eb0057d379165e957e0e5b8f.msu"
updates_alternative_links["1909"]["KB4598298"]={}
updates_alternative_links["1909"]["KB4601315"]={}
updates_alternative_links["1909"]["KB4601315"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/02/windows10.0-kb4601315-arm64_daf7220bfb212e9b8ce7251e0d2ab937eca5ab77.msu"
updates_alternative_links["1909"]["KB4601380"]={}
updates_alternative_links["1909"]["KB5000808"]={}
updates_alternative_links["1909"]["KB5000808"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/03/windows10.0-kb5000808-arm64_745f85bd767c367b5bd449db62309991dbdea8b0.msu"
updates_alternative_links["1909"]["KB5000850"]={}
updates_alternative_links["1909"]["KB5001028"]={}
updates_alternative_links["1909"]["KB5001028"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/02/windows10.0-kb5001028-arm64_b33e4550030fd6c041f405dd2679c265c6c7c7e2.msu"
updates_alternative_links["1909"]["KB5001337"]={}
updates_alternative_links["1909"]["KB5001396"]={}
updates_alternative_links["1909"]["KB5001566"]={}
updates_alternative_links["1909"]["KB5001648"]={}
updates_alternative_links["1909"]["KB5003169"]={}
updates_alternative_links["1909"]["KB5003212"]={}
updates_alternative_links["1909"]["KB5003635"]={}
updates_alternative_links["1909"]["KB5003635"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/06/windows10.0-kb5003635-arm64_c6401ff6d695e8c48bf4800f157b99a0991d0bb8.msu"
updates_alternative_links["1909"]["KB5003698"]={}
updates_alternative_links["1909"]["KB5004245"]={}
updates_alternative_links["1909"]["KB5004245"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/07/windows10.0-kb5004245-arm64_d802182a1dc38d884527aeb220daf8688dae915f.msu"
updates_alternative_links["1909"]["KB5004293"]={}
updates_alternative_links["1909"]["KB5004946"]={}
updates_alternative_links["1909"]["KB5004946"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/07/windows10.0-kb5004946-arm64_9a55b6dc7169a2f324003462ab4eeada0d7adaad.msu"
updates_alternative_links["1909"]["KB5005031"]={}
updates_alternative_links["1909"]["KB5005031"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/08/windows10.0-kb5005031-arm64_4a4cc57dd4b9abd0fd797a0c733b07a978a67831.msu"
updates_alternative_links["1909"]["KB5005103"]={}
updates_alternative_links["1909"]["KB5005566"]={}
updates_alternative_links["1909"]["KB5005566"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/09/windows10.0-kb5005566-arm64_01346cea539caa080c40c16be57f95b5c60e6501.msu"
updates_alternative_links["1909"]["KB5005624"]={}
updates_alternative_links["1909"]["KB5006667"]={}
updates_alternative_links["1909"]["KB5006667"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/10/windows10.0-kb5006667-arm64_a66ac36967336c790e1de63acadc84f1937015f5.msu"
updates_alternative_links["1909"]["KB5007189"]={}
updates_alternative_links["1909"]["KB5007189"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/11/windows10.0-kb5007189-arm64_be4e7874cdbb740f1d3a15caf99429339b11f2ce.msu"
updates_alternative_links["1909"]["KB5008206"]={}
updates_alternative_links["1909"]["KB5008206"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/12/windows10.0-kb5008206-arm64_383bf7ae2e4f714aae770de31fe19ced07b0d7fb.msu"
updates_alternative_links["1909"]["KB5009545"]={}
updates_alternative_links["1909"]["KB5009545"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2022/01/windows10.0-kb5009545-arm64_056f6095e818891f8f68499a1e2d2bc5176da932.msu"
updates_alternative_links["1909"]["KB5010345"]={}
updates_alternative_links["1909"]["KB5010345"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2022/02/windows10.0-kb5010345-arm64_7f75fa027fcaa30d7038927626d3c5b6b904da25.msu"
updates_alternative_links["1909"]["KB5010792"]={}
updates_alternative_links["1909"]["KB5011485"]={}
updates_alternative_links["1909"]["KB5011485"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2022/03/windows10.0-kb5011485-arm64_3b9b58c27979af93179bc743abd5e10478012e1d.msu"
updates_alternative_links["1909"]["KB5012591"]={}
updates_alternative_links["1909"]["KB5012591"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2022/04/windows10.0-kb5012591-arm64_f72c98a7b9c03be2d76c046925a495b887b04d44.msu"
updates_alternative_links["1909"]["KB5013945"]={}
updates_alternative_links["1909"]["KB5013945"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2022/05/windows10.0-kb5013945-arm64_77d555d9b85c5ebf65ec1bd2fd0cdb858e578afd.msu"
updates_alternative_links["2004"]={}
updates_alternative_links["2004"]["KB4557957"]={}
updates_alternative_links["2004"]["KB4557957"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/06/windows10.0-kb4557957-arm64_ee41a411a4df7deac83ad27c27fb19e5bdecfa2a.msu"
updates_alternative_links["2004"]["KB4565503"]={}
updates_alternative_links["2004"]["KB4565503"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2020/07/windows10.0-kb4565503-arm64_ffa711520def8010684296a495e8c1a7d24e447a.msu"
updates_alternative_links["2004"]["KB4566782"]={}
updates_alternative_links["2004"]["KB4566782"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/08/windows10.0-kb4566782-arm64_066598453bc1c7da637eb816b9ba5ff8ce4d7786.msu"
updates_alternative_links["2004"]["KB4567523"]={}
updates_alternative_links["2004"]["KB4568831"]={}
updates_alternative_links["2004"]["KB4571744"]={}
updates_alternative_links["2004"]["KB4571756"]={}
updates_alternative_links["2004"]["KB4571756"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/09/windows10.0-kb4571756-arm64_dc25822289e62eacff6fc3be16a50232d2e92c2d.msu"
updates_alternative_links["2004"]["KB4577063"]={}
updates_alternative_links["2004"]["KB4579311"]={}
updates_alternative_links["2004"]["KB4579311"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2020/10/windows10.0-kb4579311-arm64_71800cf51b0896e0078a9c6d3a3e7fa02ac3327b.msu"
updates_alternative_links["2004"]["KB4580364"]={}
updates_alternative_links["2004"]["KB4586781"]={}
updates_alternative_links["2004"]["KB4586781"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2020/11/windows10.0-kb4586781-arm64_a78fdfb3117982b9c47ee0783b94ea9a97b75eef.msu"
updates_alternative_links["2004"]["KB4586853"]={}
updates_alternative_links["2004"]["KB4592438"]={}
updates_alternative_links["2004"]["KB4592438"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2020/12/windows10.0-kb4592438-arm64_dc617e90333639e956453d3fc43fe02a3651cbe3.msu"
updates_alternative_links["2004"]["KB4594440"]={}
updates_alternative_links["2004"]["KB4598242"]={}
updates_alternative_links["2004"]["KB4598242"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/01/windows10.0-kb4598242-arm64_eb0931a782b8dbd7b839c7d231385dbcb008dee5.msu"
updates_alternative_links["2004"]["KB4598291"]={}
updates_alternative_links["2004"]["KB4601319"]={}
updates_alternative_links["2004"]["KB4601319"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/02/windows10.0-kb4601319-arm64_af460351b77a7e2620007303da65151916e44a22.msu"
updates_alternative_links["2004"]["KB4601382"]={}
updates_alternative_links["2004"]["KB5000802"]={}
updates_alternative_links["2004"]["KB5000802"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/03/windows10.0-kb5000802-arm64_5a9e0d3563cf0c86f61c75a58d53eeda7f0fbfc1.msu"
updates_alternative_links["2004"]["KB5000842"]={}
updates_alternative_links["2004"]["KB5001330"]={}
updates_alternative_links["2004"]["KB5001330"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/04/windows10.0-kb5001330-arm64_6e2a532b4f24bd3a771bca0013b9e09084181ae6.msu"
updates_alternative_links["2004"]["KB5001391"]={}
updates_alternative_links["2004"]["KB5001567"]={}
updates_alternative_links["2004"]["KB5001649"]={}
updates_alternative_links["2004"]["KB5003173"]={}
updates_alternative_links["2004"]["KB5003173"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/05/windows10.0-kb5003173-arm64_6d39d557af0eb2bf39a18883bb2d61a69337b29e.msu"
updates_alternative_links["2004"]["KB5003214"]={}
updates_alternative_links["2004"]["KB5003637"]={}
updates_alternative_links["2004"]["KB5003637"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/06/windows10.0-kb5003637-arm64_39ead83121a6c9cb27938f2be87878fd2623d7b2.msu"
updates_alternative_links["2004"]["KB5003690"]={}
updates_alternative_links["2004"]["KB5003690"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/updt/2021/06/windows10.0-kb5003690-arm64_923ae1d8d5ee2e1794e93a0fc94afe6c8bf7e640.msu"
updates_alternative_links["2004"]["KB5004237"]={}
updates_alternative_links["2004"]["KB5004237"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/07/windows10.0-kb5004237-arm64_befe5aaac7ac7802c9af4fda34714a30123c8059.msu"
updates_alternative_links["2004"]["KB5004296"]={}
updates_alternative_links["2004"]["KB5004476"]={}
updates_alternative_links["2004"]["KB5004760"]={}
updates_alternative_links["2004"]["KB5004945"]={}
updates_alternative_links["2004"]["KB5004945"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/07/windows10.0-kb5004945-arm64_7ea91a632f2fb0f3b32136c9ad4786ff7cd47f7c.msu"
updates_alternative_links["2004"]["KB5005033"]={}
updates_alternative_links["2004"]["KB5005033"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/08/windows10.0-kb5005033-arm64_ff1297a73f8e39efd4e32892206a92e0fa8b8e4c.msu"
updates_alternative_links["2004"]["KB5005101"]={}
updates_alternative_links["2004"]["KB5005565"]={}
updates_alternative_links["2004"]["KB5005565"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2021/09/windows10.0-kb5005565-arm64_3466d089a8a8e11b92849cd1984accac4e90f22f.msu"
updates_alternative_links["2004"]["KB5005611"]={}
updates_alternative_links["2004"]["KB5006670"]={}
updates_alternative_links["2004"]["KB5006670"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2021/10/windows10.0-kb5006670-arm64_c91c87a424499a4051b66026ed73bb4dda7bc9d7.msu"
updates_alternative_links["2004"]["KB5006738"]={}
updates_alternative_links["2004"]["KB5007186"]={}
updates_alternative_links["2004"]["KB5007253"]={}
updates_alternative_links["2004"]["KB5008212"]={}
updates_alternative_links["11-21H2"]={}
updates_alternative_links["11-21H2"]["KB5012643"]={}
updates_alternative_links["11-21H2"]["KB5012643"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/updt/2022/04/windows10.0-kb5012643-arm64_26ae3882c036a817235c8e9be57407dae7f957ec.msu"
updates_alternative_links["11-21H2"]["KB5013943"]={}
updates_alternative_links["11-21H2"]["KB5014019"]={}
updates_alternative_links["11-21H2"]["KB5014668"]={}
updates_alternative_links["11-21H2"]["KB5014697"]={}
updates_alternative_links["11-21H2"]["KB5014697"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2022/06/windows10.0-kb5014697-arm64_e435989dee5f7b993fc1556d0a9e6e555b0efc6c.msu"
updates_alternative_links["20H2"]={}
updates_alternative_links["20H2"]["KB5009543"]={}
updates_alternative_links["20H2"]["KB5009543"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2022/01/windows10.0-kb5009543-arm64_ccb044e3c73cc8a621746b61f464d80cd2794fa7.msu"
updates_alternative_links["20H2"]["KB5009596"]={}
updates_alternative_links["20H2"]["KB5010342"]={}
updates_alternative_links["20H2"]["KB5010342"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2022/02/windows10.0-kb5010342-arm64_27a61a2ac9924f7c753b5e25df8a5dcab4681eee.msu"
updates_alternative_links["20H2"]["KB5010415"]={}
updates_alternative_links["20H2"]["KB5010793"]={}
updates_alternative_links["20H2"]["KB5011487"]={}
updates_alternative_links["20H2"]["KB5011543"]={}
updates_alternative_links["20H2"]["KB5011831"]={}
updates_alternative_links["20H2"]["KB5012599"]={}
updates_alternative_links["20H2"]["KB5013942"]={}
updates_alternative_links["20H2"]["KB5014023"]={}
updates_alternative_links["20H2"]["KB5014666"]={}
updates_alternative_links["20H2"]["KB5014699"]={}
updates_alternative_links["20H2"]["KB5014699"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2022/06/windows10.0-kb5014699-arm64_ca2074dc96dbf5e74aee768322b417877bd0835d.msu"
updates_alternative_links["20H2"]["KB5015020"]={}
updates_alternative_links["20H2"]["KB5015807"]={}
updates_alternative_links["20H2"]["KB5015807"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2022/07/windows10.0-kb5015807-arm64_f74ff1640344c14158a787c593ed9b2cdf4f81cd.msu"
updates_alternative_links["20H2"]["KB5015878"]={}
updates_alternative_links["20H2"]["KB5016139"]={}
updates_alternative_links["20H2"]["KB5016139"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2022/06/windows10.0-kb5016139-arm64_73bbf3e340801f3c1c399ee60b5ee352e3afc934.msu"
updates_alternative_links["20H2"]["KB5016616"]={}
updates_alternative_links["20H2"]["KB5016688"]={}
updates_alternative_links["20H2"]["KB5017308"]={}
updates_alternative_links["20H2"]["KB5017308"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2022/09/windows10.0-kb5017308-arm64_1ca51a0b3abdab7ee891bd1e1e6d3f03bc15e324.msu"
updates_alternative_links["20H2"]["KB5017380"]={}
updates_alternative_links["20H2"]["KB5018410"]={}
updates_alternative_links["20H2"]["KB5018410"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2022/10/windows10.0-kb5018410-arm64_a0d4c6caf83af34442728052eb3e1002add312fb.msu"
updates_alternative_links["20H2"]["KB5018482"]={}
updates_alternative_links["20H2"]["KB5019275"]={}
updates_alternative_links["20H2"]["KB5019959"]={}
updates_alternative_links["20H2"]["KB5020030"]={}
updates_alternative_links["20H2"]["KB5020435"]={}
updates_alternative_links["20H2"]["KB5020953"]={}
updates_alternative_links["20H2"]["KB5021233"]={}
updates_alternative_links["20H2"]["KB5021233"]["arm64"]="https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2022/12/windows10.0-kb5021233-arm64_4bac0de318c939e54fa6a9f537e892272446ae09.msu"
updates_alternative_links["20H2"]["KB5022282"]={}
updates_alternative_links["20H2"]["KB5022282"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2023/01/windows10.0-kb5022282-arm64_9ccaddc4356ab1db614881e08635bd8959ff97f3.msu"
updates_alternative_links["20H2"]["KB5022834"]={}
updates_alternative_links["20H2"]["KB5022834"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2023/02/windows10.0-kb5022834-arm64_2424bbabd00263d4c2181036158935fc64611ce9.msu"
updates_alternative_links["20H2"]["KB5022906"]={}
updates_alternative_links["20H2"]["KB5023696"]={}
updates_alternative_links["20H2"]["KB5023696"]["arm64"]="https://catalog.s.download.windowsupdate.com/d/msdownload/update/software/secu/2023/03/windows10.0-kb5023696-arm64_ad35eba7793223b4398a02543bb0df79fc5370fb.msu"
updates_alternative_links["20H2"]["KB5023773"]={}
updates_alternative_links["20H2"]["KB5025221"]={}
updates_alternative_links["20H2"]["KB5026361"]={}

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
