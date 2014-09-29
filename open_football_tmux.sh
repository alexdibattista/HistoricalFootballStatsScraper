#!/usr/bin/tmux source-file

tmux new-session -d
tmux split-window -d -t 0 -v
tmux split-window -d -t 0 -h
tmux split-window -d -t 0 -v
tmux split-window -d -t 2 -v

tmux send-keys -t 0 "cd ~/Documents/\"Personal Projects\"/OpenFootball" enter
tmux send-keys -t 0 "nodemon" enter

tmux send-keys -t 3 "cd ~/Documents/\"Personal Projects\"/OpenFootball" enter
tmux send-keys -t 3 "mongo" enter

tmux send-keys -t 2 "sudo mongod --dbpath /mongo/db/" enter


tmux send-keys -t 4 "cd ~/Documents/\"Personal Projects\"/OpenFootball" enter

tmux select-pane -t 4

tmux attach