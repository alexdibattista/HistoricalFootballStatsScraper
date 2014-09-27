setup_tmux_layout() {
  tmux -new-window -a -n "$1" -c "$2"

  tmux split-window -h
  tmux split-window -v

}

open_football_project() {
  tmux new-window -a -n "$2" -c "$1"

  tmux send-keys "cd $2"

  tmux split-window -h -c "$1"
}