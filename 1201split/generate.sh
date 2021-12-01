#!/usr/bin/bash

set -e

# python3 lac_full_text.py ../docs/chq/bao_lian_deng.txt chq bao_lian_deng
# python3 lac_full_text.py ../docs/chq/bo_ya*.txt chq bo_ya
# python3 lac_full_text.py ../docs/chq/gong_gong*.txt chq gong_gong
# python3 lac_full_text.py ../docs/chq/hua_*.txt chq hua_mu_lan
# python3 lac_full_text.py ../docs/chq/jiao_*.txt chq jiao_zhong
# python3 lac_full_text.py ../docs/chq/li_wa*.txt chq li_wa
# python3 lac_full_text.py ../docs/chq/nv_*.txt chq nv_wa_de_gu_shi
# python3 lac_full_text.py ../docs/chq/qin_*.txt chq qin_shi
# python3 lac_full_text.py ../docs/chq/wo_*.txt chq wo_xin

python3 lac_full_text.py ../docs/hyf/cuo_*.txt hyf cuo_cuo_cuo
python3 lac_full_text.py ../docs/hyf/di_san_*.txt hyf di_san_zhi
python3 lac_full_text.py ../docs/hyf/dian_nao.txt hyf dian_nao
python3 lac_full_text.py ../docs/hyf/hua_*.txt hyf hua_pi
python3 lac_full_text.py ../docs/hyf/liang_*.txt hyf liang_ge_hai_zi
python3 lac_full_text.py ../docs/hyf/liu_*.txt hyf liu_zai_zhong
python3 lac_full_text.py ../docs/hyf/qing_*.txt hyf qing_feng
python3 lac_full_text.py ../docs/hyf/ru_*.txt hyf ru_guo
python3 lac_full_text.py ../docs/hyf/wo_*.txt hyf wo_ke