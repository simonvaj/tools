
alias gs='git status'
alias gl='git log'
alias gsl='git shortlog'
#alias gflow='git log --graph --decorate --oneline --first-parent --format=format:"%C(bold blue)%h%C(reset) %<(52,trunc)%C(white)%s%C(reset) %C(bold green)(%ai)%C(reset) %C(red)[%an] %C(bold yellow)%d%C(reset)"'
alias gw='git log --graph --decorate --oneline --first-parent --format=format:"%C(bold blue)%h%C(reset) %<(52,trunc)%C(white)%s%C(reset) %C(red)[%an] %C(bold yellow)%d%C(reset)"'
alias gww='gw -20'
alias gt='git log --graph --abbrev-commit --decorate --first-parent --format=format:"%C(bold blue)%h%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset) %C(red)- %an%C(reset)%n""          %C(white)%s%C(reset)" --all'
alias gtt='gt -20'
alias gd='git diff'

alias gc='git commit'
alias gcv='git commit --verbose'
alias gcm='git commit -m'
alias gca='git commit --amend'
alias gcae='git commit --amend --no-edit'

# git add .          stages new files and modifications, without deletions
# git add --update   stages modifications and deletions, without new files
# git add --all      stages all changes, equivalent to git add .; git add -u
alias ga='git add'
alias gaa='git add --all'
alias gau='git add --update'
alias gap='git add --patch'
alias gae='git add --edit'
alias gai='git add --interactive'

alias gsh='git stash'
alias gsha='git stash apply'
alias gshp='git stash pop'
alias gshl='git stash list'

alias gf='git fetch --prune'
alias gu='git push'
alias gn='git pull'
alias grb='git rebase'
alias grbi='git rebase --interactive'
alias gm='git merge'

alias gj='git checkout'
alias gjb='git checkout -b'
alias gb='git branch'

alias gp='git cherry-pick'