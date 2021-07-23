cd ../Resources/k-folds/partitioned_data/raw_partition

cat 1_en.txt 2_en.txt 3_en.txt 4_en.txt > ../5_en_cat.txt
cat 2_en.txt 3_en.txt 4_en.txt 5_en.txt > ../1_en_cat.txt
cat 1_en.txt 3_en.txt 4_en.txt 5_en.txt > ../2_en_cat.txt
cat 1_en.txt 2_en.txt 4_en.txt 5_en.txt > ../3_en_cat.txt
cat 1_en.txt 2_en.txt 3_en.txt 5_en.txt > ../4_en_cat.txt

cat 1_zhs.txt 2_zhs.txt 3_zhs.txt 4_zhs.txt > ../5_zhs_cat.txt
cat 2_zhs.txt 3_zhs.txt 4_zhs.txt 5_zhs.txt > ../1_zhs_cat.txt
cat 1_zhs.txt 3_zhs.txt 4_zhs.txt 5_zhs.txt > ../2_zhs_cat.txt
cat 1_zhs.txt 2_zhs.txt 4_zhs.txt 5_zhs.txt > ../3_zhs_cat.txt
cat 1_zhs.txt 2_zhs.txt 3_zhs.txt 5_zhs.txt > ../4_zhs_cat.txt