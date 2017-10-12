set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=$HOME/.vim/bundle/Vundle.vim/
call vundle#begin('$HOME/.vim/bundle/')
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'

" git diff in sign column
Plugin 'airblade/vim-gitgutter'

" added nerdtree
Plugin 'scrooloose/nerdtree'

" syntastic for error checking
Plugin 'vim-syntastic/syntastic'

" easymotion for easy navigation in files
Plugin 'easymotion/vim-easymotion'

" willy colorscheme
" colorscheme willy-light
" colorscheme willy-dark
Plugin 'nightsense/willy'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line


""""""""" NERDtree
" Load NERDtree
autocmd vimenter * NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Load pathogen
"filetype off
"call pathogen#incubate()
"execute pathogen#infect()
"call pathogen#helptags()

""" Set start window position and size
"winpos 33 0
"set lines=60

""" Set the tab to 4 spaces. 
:set tabstop=4
:set shiftwidth=4
:set expandtab

:set smartindent

""" Show line number.
:set number

" Change leader key from \
let mapleader=" "

" shortcut to easy-motion
map <leader>v <leader><leader>w

" Quickly edit/reload the vimrc file using ,ev and ,sv
nmap <silent> <leader>ev :e $MYVIMRC<CR>
nmap <silent> <leader>sv :so $MYVIMRC<CR>

highlight Folded guibg=black guifg=blue
highlight FoldColumn guibg=darkgrey guifg=white

set backspace=indent,eol,start

:filetype plugin on
filetype plugin indent on
syntax on

inoremap <s-tab> <c-d>
:nmap <S-BS> <<
" :inoremap <S-BS> <BS><BS><BS><BS>

set nobackup
set noswapfile

" Vim can highlight whitespaces for you in a convenient way:
set list
set listchars=tab:>.,trail:.,extends:#,nbsp:.
" This line will make Vim set out tab characters, trailing whitespace and
" invisible spaces visually, and additionally use the # sign at the end of
" lines to mark lines that extend off-screen. For more info, see :h listchars.
autocmd filetype html,xml set listchars-=tab:>.


noremap <C-tab> gt

" Reselect visual block after indent/outdent
vnoremap < <gv
vnoremap > >gv

" Make alt keys only for mappings
set winaltkeys=no

" Easy split navigation
nnoremap <A-h> <C-w>h
nnoremap <A-j> <C-w>j
nnoremap <A-k> <C-w>k
nnoremap <A-l> <C-w>l

" Improve up/down movement on wrapped lines.
nnoremap j gj
nnoremap k gk

" Automatically reload vimrc when it is saved.
" au BufWritePost .vimrc so ~/.vimrc

" Remap the escape key.
inoremap jk <Esc>

" Remap saving to Ctrl-S 
nnoremap <C-s> :w<CR>
inoremap <C-s> <Esc>:w<CR><Insert>

" Set font
if has('gui_running')
:set guifont=Consolas:h9
endif

" Resize window of vertical split
:map - <C-W>-
:map + <C-W>+

" Go to next window
:map <F6> <C-W>w

" Set mouse ON
:set mouse=a

" Buffer commands
" nnoremap ,b :ls<CR>:buffer<Space>

" the following command maps the <F5> key to search for the keyword under the cursor in the current directory using the 'grep' command:
"nnoremap <F5> :grep <C-R><C-W> *<CR>

nnoremap ; ,
nnoremap , ;

""""""""""""""""""""""""""" Concerns searching """""""""""""""""""""""""""""""""
set incsearch
set ignorecase
set smartcase
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"nnoremap <space> za
"set foldmethod=syntax "indent

" Enable syntax highlighting when it is available
"if &t_Co > 1
"    syntax enable
"endif

colorscheme willy-light
set statusline=%<%f\ %h%m%r%=%-14.(%l,%c%V%)\ %P

""""""""" syntastic error checking """""""""""""""""""""""""""""""""""
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""" vim fugitive (git) """"""""""""""""""""""""""""""""""""""""
nnoremap <leader>gs :Gstatus<CR>
nnoremap <leader>gc :Gcommit -v -q<CR>
nnoremap <leader>ga :Gcommit --amend<CR>
nnoremap <leader>gt :Gcommit -v -q %<CR>
nnoremap <leader>gd :Gvdiff<CR>
nnoremap <leader>ge :Gedit<CR>
nnoremap <leader>gr :Gread<CR>
nnoremap <leader>gw :Gwrite<CR><CR>
nnoremap <leader>gl :silent! Glog<CR>
nnoremap <leader>gp :Ggrep<Space>
nnoremap <leader>gm :Gmove<Space>
nnoremap <leader>gb :Git branch<Space>
nnoremap <leader>go :Git checkout<Space>
nnoremap <leader>gps :Dispatch! git push<CR>
nnoremap <leader>gpl :Dispatch! git pull<CR>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""" diff """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nmap ö [c
nmap ä ]c
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

noremap <C-h> ^
noremap <C-l> $
noremap <C-j> b
noremap <C-k> w

nnoremap <C-u> 25k
nnoremap <C-d> 25j

inoremap <C-h> <Left>
inoremap <C-j> <Down>
inoremap <C-k> <Up>
inoremap <C-l> <Right>
