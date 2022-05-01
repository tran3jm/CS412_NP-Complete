lineBreak="-------------------------------------------"

rm -rf ./output
rm -rf ./generated
mkdir -p ./output
mkdir -p ./generated

echo "MIN VERTEX COVER TESTS"
echo $lineBreak
echo "KNOWN TESTS"
echo $lineBreak

for file in test*.txt; do
echo "EXACT $(basename $file .txt)"
python ../vertex_cover/exact_solution/exact.py < $file > ./output/known_exact_$file
done

echo ""
for file in test*.txt; do
echo "APPROX $(basename $file .txt)"
python ../vertex_cover/approx_solution/approx.py < $file > ./output/known_approx_$file
done

echo $lineBreak
echo "GENERATED TESTS"
echo $lineBreak
for ((i = 1; i <= 20; i++)); do
python ./cs412TestGen.py $i > ./generated/generated_test$i.txt
done

for file in ./generated/generated_test*.txt; do
fileName=$(basename $file)
echo "EXACT $(basename $file .txt)"
python ../vertex_cover/exact_solution/exact.py < $file > ./output/exact_$fileName
done

echo ""
for file in ./generated/generated_test*.txt; do
fileName=$(basename $file)
echo "APPROX $(basename $file .txt)"
python ../vertex_cover/approx_solution/approx.py < $file > ./output/approx_$fileName
done
echo $lineBreak
echo "Generated tests can be found in ./generated/"
echo "Test output with runtime can be found in ./output/"