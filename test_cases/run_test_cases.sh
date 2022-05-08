lineBreak="-------------------------------------------"
#! /usr/bin/env python
rm -rf ./output
rm -rf ./generated
mkdir -p ./output
mkdir -p ./generated
 
echo "MIN VERTEX COVER TESTS"
echo $lineBreak
echo "KNOWN TESTS"
echo $lineBreak
 
# for file in test*.txt; do
# # # echo "EXACT $(basename $file .txt)"
# # python ../vertex_cover/exact_solution/exact.py < $file > ./output/known_exact_$file
 
# # # echo "APPROX $(basename $file .txt)"
# # python ../vertex_cover/approx_solution/approx.py < $file > ./output/known_approx_$file
 
#     fileName=$(basename $file)
#     # echo "EXACT $(basename $file .txt)"
#     python ../vertex_cover/exact_solution/exact.py < $file > ./output/known_exact_$file
#     exact_output=$(cat ./output/known_exact_$file | head -n1 | sed 's/Min number: //')
#     exact_runtime=$(cat ./output/known_exact_$file | tail -n1)
#     fileName=$(basename $file)
#     # echo "APPROX $(basename $file .txt)"
#     python ../vertex_cover/approx_solution/approx.py < $file > ./output/known_approx_$file
#     approx_output=$(cat ./output/known_approx_$file | head -n1 | sed 's/Min number: //')
#     approx_runtime=$(cat ./output/known_approx_$file | tail -n1)
#     echo $fileName
#     echo "EXACT: $exact_output in $exact_runtime"
#     echo "APPROX: $approx_output in $approx_runtime"
#     if [ "$exact_output" == "There are no edges." ] || [ "$approx_output" == "There are no edges." ]; then
#         if [ "$exact_output" == "$approx_output" ]; then
#             echo "PASS"
#         else
#             echo "FAIL"
#         fi
#     elif ! python compare_bounds.py $approx_output $exact_output; then
#         echo "$approx_output <= 2*$exact_output"
#         echo "PASS"
#     else
#         echo "$approx_output > 2*$exact_output"
#         echo "FAIL"
#     fi
#     echo ""
# done
 
echo $lineBreak
echo "GENERATED TESTS"
echo $lineBreak
for ((i = 1; i <= 20; i++)); do
python ./cs412TestGen.py $i > ./generated/generated_test$i.txt
done
 
for file in ./generated/generated_test*.txt; do
   fileName=$(basename $file)
   # echo "EXACT $(basename $file .txt)"
   python ../vertex_cover/exact_solution/exact.py < $file > ./output/exact_$fileName
   exact_output=$(cat ./output/exact_$fileName | head -n1 | sed 's/Min number: //')
   exact_runtime=$(cat ./output/exact_$fileName | tail -n1)
   fileName=$(basename $file)
   # echo "APPROX $(basename $file .txt)"
   python ../vertex_cover/approx_solution/approx.py < $file > ./output/approx_$fileName
   approx_output=$(cat ./output/approx_$fileName | head -n1 | sed 's/Min number: //')
   approx_runtime=$(cat ./output/approx_$fileName | tail -n1)
   echo $fileName
   echo "EXACT: $exact_output in $exact_runtime"
   echo "APPROX: $approx_output in $approx_runtime"
   if [ "$exact_output" == "There are no edges." ] || [ "$approx_output" == "There are no edges." ]; then
       if [ "$exact_output" == "$approx_output" ]; then
           echo "PASS"
       else
           echo "FAIL"
       fi
   elif ! python compare_bounds.py $approx_output $exact_output; then
       echo "$approx_output <= 2*$exact_output"
       echo "PASS"
   else
       echo "$approx_output > 2*$exact_output"
       echo "FAIL"
   fi
   echo ""
done
echo $lineBreak
echo "Generated tests can be found in ./generated/"
echo "Test output with runtime can be found in ./output/"


declare -a AVERAGE_APPROXTIME=()
declare -a AVERAGE_EXACTTIME=()
COUNTER=0

# manual graph tests
echo $lineBreak
echo "GRAPH MANUAL TESTS"
echo $lineBreak
 
for file in ./manual_test/mtest*.txt; do
   ((COUNTER=COUNTER+1))
   fileName=$(basename $file)
   # echo "EXACT $(basename $file .txt)"
   python ../vertex_cover/exact_solution/exact.py < $file > ./output/exact_$fileName
   exact_output=$(cat ./output/exact_$fileName | head -n1 | sed 's/Min number: //')
   exact_runtime=$(cat ./output/exact_$fileName | tail -n1)
   fileName=$(basename $file)
   # echo "APPROX $(basename $file .txt)"
   python ../vertex_cover/approx_solution/approx.py < $file > ./output/approx_$fileName
   approx_output=$(cat ./output/approx_$fileName | head -n1 | sed 's/Min number: //')
   approx_runtime=$(cat ./output/approx_$fileName | tail -n1)
   echo $fileName
   echo "EXACT: $exact_output in $exact_runtime"
   echo "APPROX: $approx_output in $approx_runtime"
   if [ "$exact_output" == "There are no edges." ] || [ "$approx_output" == "There are no edges." ]; then
       if [ "$exact_output" == "$approx_output" ]; then
           echo "PASS"
       else
           echo "FAIL"
       fi
   elif ! python compare_bounds.py $approx_output $exact_output; then
       echo "$approx_output <= 2*$exact_output"
       echo "PASS"
   else
       echo "$approx_output > 2*$exact_output"
       echo "FAIL"
   fi
   AVERAGE_APPROXTIME+=($approx_output)
   AVERAGE_EXACTTIME+=($exact_output)
 
   if [$(expr $COUNTER % 4) == "0"]; then
       approxsum=0
       exactsum=0
       for i in "${AVERAGE_APPROXTIME[@]}"
       do
           ((approxsum=approxsum+i))
       done
 
       for i in "${AVERAGE_EXACTTIME[@]}"
       do
           ((exactsum=exactsum+i))
       done
       echo "Average runtime for approximate: $(($approxsum / 4))"
       echo "Average runtime for exact: $(($exactsum / 4))"
       AVERAGE_APPROXTIME=()
       AVERAGE_EXACTTIME=()
   fi
   echo ""
done
echo $lineBreak
echo "Generated tests can be found in ./generated/"
echo "Test output with runtime can be found in ./output/"