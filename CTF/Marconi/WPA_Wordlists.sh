#!/bin/bash

echo "Starting Wordlist creation:"

echo "Makes creation:"
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words1.txt -t makes@metal@magic@magma
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words2.txt -t makes@metal@magma@magic
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words3.txt -t makes@magic@metal@magma
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words4.txt -t makes@magic@magma@metal
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words5.txt -t makes@magma@magic@metal
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words6.txt -t makes@magma@metal@magic

cat words1.txt words2.txt words3.txt words4.txt words5.txt words6.txt > Makes.txt

echo "Metal Creation:"
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words1.txt -t metal@makes@magic@magma
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words2.txt -t metal@makes@magma@magic
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words3.txt -t metal@magic@makes@magma
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words4.txt -t metal@magic@magma@makes
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words5.txt -t metal@magma@magic@makes
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words6.txt -t metal@magma@makes@magic

cat words1.txt words2.txt words3.txt words4.txt words5.txt words6.txt > Metal.txt

echo "Magic Creation:"
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words1.txt -t magic@makes@metal@magma
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words2.txt -t magic@makes@magma@metal
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words3.txt -t magic@metal@makes@magma
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words4.txt -t magic@metal@magma@makes
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words5.txt -t magic@magma@metal@makes
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words6.txt -t magic@magma@makes@metal

cat words1.txt words2.txt words3.txt words4.txt words5.txt words6.txt > Magic.txt

echo "Magma Creation:"
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words1.txt -t magma@makes@metal@magic
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words2.txt -t magma@makes@magic@metal
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words3.txt -t magma@metal@makes@magic
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words4.txt -t magma@metal@magic@makes
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words5.txt -t magma@magic@metal@makes
crunch 23 23 -f /usr/share/crunch/charset.lst symbols-all -o words6.txt -t magma@magic@makes@metal

cat words1.txt words2.txt words3.txt words4.txt words5.txt words6.txt > Magma.txt

echo "Combine into single file:"

cat Makes.txt Metal.txt Magic.txt Magma.txt > WPA_Marconi_Dictionary.txt

rm words1.txt
rm words2.txt
rm words3.txt
rm words4.txt
rm words5.txt
rm words6.txt
rm Makes.txt
rm Metal.txt
rm Magic.txt
rm Magma.txt

echo "Done"
