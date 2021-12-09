#!/usr/bin/bash

set -e

# python3 lac_full_text.py ../docs/chq/bao_lian_deng.txt chq bao_lian_deng /home/hulj/workspace/lg/a
# python3 lac_full_text.py ../docs/chq/bo_ya*.txt chq bo_ya /home/hulj/workspace/lg/all_unique
# python3 lac_full_text.py ../docs/chq/gong_gong*.txt chq gong_gong /home/hulj/workspace/lg/all_unique
# python3 lac_full_text.py ../docs/chq/hua_*.txt chq hua_mu_lan /home/hulj/workspace/lg/all_unique
# python3 lac_full_text.py ../docs/chq/jiao_*.txt chq jiao_zhong /home/hulj/workspace/lg/all_unique
# python3 lac_full_text.py ../docs/chq/li_wa*.txt chq li_wa /home/hulj/workspace/lg/all_unique
# python3 lac_full_text.py ../docs/chq/nv_*.txt chq nv_wa_de_gu_shi /home/hulj/workspace/lg/all_unique
# python3 lac_full_text.py ../docs/chq/qin_*.txt chq qin_shi /home/hulj/workspace/lg/all_unique
# python3 lac_full_text.py ../docs/chq/wo_*.txt chq wo_xin /home/hulj/workspace/lg/all_unique

python3 lac_full_text.py ../docs/hyf/cuo_*.txt hyf cuo_cuo_cuo /home/hulj/workspace/lg/all_unique
python3 lac_full_text.py ../docs/hyf/di_san_*.txt hyf di_san_zhi /home/hulj/workspace/lg/all_unique
python3 lac_full_text.py ../docs/hyf/dian_nao.txt hyf dian_nao /home/hulj/workspace/lg/all_unique
python3 lac_full_text.py ../docs/hyf/hua_*.txt hyf hua_pi /home/hulj/workspace/lg/all_unique
python3 lac_full_text.py ../docs/hyf/liang_*.txt hyf liang_ge_hai_zi /home/hulj/workspace/lg/all_unique
python3 lac_full_text.py ../docs/hyf/liu_*.txt hyf liu_zai_zhong /home/hulj/workspace/lg/all_unique
python3 lac_full_text.py ../docs/hyf/qing_*.txt hyf qing_feng /home/hulj/workspace/lg/all_unique
python3 lac_full_text.py ../docs/hyf/ru_*.txt hyf ru_guo /home/hulj/workspace/lg/all_unique
python3 lac_full_text.py ../docs/hyf/wo_*.txt hyf wo_ke /home/hulj/workspace/lg/all_unique