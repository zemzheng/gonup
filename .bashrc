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
complete -W "`python ~/complete.py go`" go
complete -W "`python ~/complete.py up`" up
