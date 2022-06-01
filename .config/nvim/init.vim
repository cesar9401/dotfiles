set number "muestra los numeros de linea

set title "muestra el nombre del archivo en la terminal
set mouse=a "permite la integracion del mouse(seleccionar texto, mover el cursor)

syntax enable
set clipboard=unnamedplus

set nowrap "no dividir la linea si es muy larga
" set cursorline "resalta la linea actual
set autoindent "para usar la indentacion de la linea previa en la nueva linea
set ruler "siempre muestra la posicion del cursor
set showcmd "Display an incomplete command in the lower right corner of the Vim window
"set incsearch " Display matches for a search pattern while you type.

filetype plugin indent on
syntax on
set t_Co=256

set tabstop=4
set shiftwidth=4
set softtabstop=4
set shiftround
set expandtab
set smarttab
set background=dark
set cursorline
autocmd InsertEnter * highlight CursorLine guibg=#000050 guifg=fg
autocmd InsertLeave * highlight CursorLine guibg=#004000 guifg=fg

" set cursorcolumn
set completeopt=noinsert,menuone,noselect  
set hidden
set inccommand=split
" set relativenumber
set splitbelow splitright
set timeoutlen=0
set wildmenu
set termguicolors

" italics
let &t_ZH="\e[3m"
let &t_ZR="\e[23m"

" file browser
let g:netrw_banner=0
let g:netrw_liststyle=3
let g:netrw_browse_split=3
let g:netrw_altv=1
let g:netrw_winsize=25
let g:netrw_keepdir=0
let g:netrw_localcopydircmd='cp -r'
set autochdir
map <C-E> :Lexplore<CR>
