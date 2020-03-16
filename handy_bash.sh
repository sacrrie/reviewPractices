#batch move same type of files in a group of similiarly named folders

#this S1* means all folders begin with S1
for folder in S1*; do
	#this means all the zip file
	for file in "$folder"/*.zip; do
		#the path here is relative 
		#to the path where the bash is
		#executed.
		mv "$file" "./archive/"
	done
done
