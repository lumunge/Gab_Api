rm -rf json;
mkdir json;
cd json; 
mkdir BLJson LLJson PLJson SAJson;
cd ../;
python3 fetch_data.py
cd ../;
python3 manage.py runscript store_data;
