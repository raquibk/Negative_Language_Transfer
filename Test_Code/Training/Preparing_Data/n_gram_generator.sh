cd /home/raquib/Documents/Setups/kenlm/build
file_en_ext="_en.arpa"
file_zhs_ext="_zhs.arpa"
for ((i = 2; i<=6; i++)); do
    bin/lmplz -o $i <../../../../Desktop/EdTekla/Negative_Language_Transfer/Test_Code/Resources/en_ud.txt > ../../../../Desktop/EdTekla/Negative_Language_Transfer/Test_Code/Resources/n_gram_models/$i$file_en_ext --discount_fallback
    bin/lmplz -o $i <../../../../Desktop/EdTekla/Negative_Language_Transfer/Test_Code/Resources/zhs_ud.txt > ../../../../Desktop/EdTekla/Negative_Language_Transfer/Test_Code/Resources/n_gram_models/$i$file_zhs_ext --discount_fallback
done