cd /home/raquib/Documents/Setups/kenlm/build
cat_en_ext="_en_cat.txt"
cat_zhs_ext="_zhs_cat.txt"
n_ext="n_"
output_en_ext="en.arpa"
output_zhs_ext="zhs.arpa"

for ((i = 2; i<=6; i++)); do
    for ((k = 1; k<=5; k++)); do
        bin/lmplz -o $i <../../../../Desktop/EdTekla/Negative_Language_Transfer/Test_Code/Resources/k-folds/partitioned_data/$k$cat_en_ext > ../../../../Desktop/EdTekla/Negative_Language_Transfer/Test_Code/Resources/k-folds/LMs/$i$n_ext$k$output_en_ext --discount_fallback
        bin/lmplz -o $i <../../../../Desktop/EdTekla/Negative_Language_Transfer/Test_Code/Resources/k-folds/partitioned_data/$k$cat_zhs_ext > ../../../../Desktop/EdTekla/Negative_Language_Transfer/Test_Code/Resources/k-folds/LMs/$i$n_ext$k$output_zhs_ext --discount_fallback
        done
    done
