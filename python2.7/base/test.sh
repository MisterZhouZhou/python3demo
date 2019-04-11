tiss=$(cat config.json | grep version | head -1 | awk -F: '{ print $2 }' | sed 's/[\",]//g' | tr -d '[[:space:]]')
echo ${tiss}




if [[ $tiss == "1.0.3" ]]; then
  echo 'dd'
fi