function go(){
    cd ~/gonup
    python ./go.py $*
    cd -
}
function up(){
    cd ~/gonup
    python ./update.py $*
    cd -
}
