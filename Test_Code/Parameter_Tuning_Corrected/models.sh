cd /home/raquib/Documents/Setups/kenlm/build
cat_en_ext="_en_cat.txt"
cat_zhs_ext="_zhs_cat.txt"
n_ext="n_"
output_en_ext="en.arpa"
output_zhs_ext="zhs.arpa"

for ((i = 2; i<=6; i++)); do
    for ((k = 1; k<=5; k++)); do
        bin/lmplz -o $i <../../../../Desktop/k_folds_x/English/Concatenated/$k$cat_en_ext > ../../../../Desktop/k_folds_x/LMs/$i$n_ext$k$output_en_ext --discount_fallback
        bin/lmplz -o $i <../../../../Desktop/k_folds_x/Chinese/Concatenated/$k$cat_zhs_ext > ../../../../Desktop/k_folds_x/LMs/$i$n_ext$k$output_zhs_ext --discount_fallback
        done
    done