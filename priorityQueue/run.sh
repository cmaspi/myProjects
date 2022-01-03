set -x initial (sha1sum priority.csv)
gedit priority.csv
set -x final (sha1sum priority.csv)

while [ $initial != $final ]
echo $initial
echo $final
python3 queue.py
set -x initial (sha1sum priority.csv)
gedit priority.csv
set -x final (sha1sum priority.csv)
end
