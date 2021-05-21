title: VIM for Python development (and not only)
date: 06-05-2020 12:59
description: My VIM setup for writing Python and other things.
thumbnail: images/vim_01.png

<center>
<img src="{static}/images/vim_01.png" alt="Vim" style="">
</center>

*__tl;dr__: This is a write up on how and why I use the famously hard-to-use VIM text editor.*

- *Skip to [here](#general-vim-setup) if you already know VIM.*
- *Jump to the [python specific section](#vim-for-python-development).*
- *See my [.vimrc](#my-vimrc).*
- *Get my [dotfiles](https://github.com/duarteocarmo/dotfiles).*


## What the hell is VIM?


We're all used to use our mouse to click around a document. You click on a character to go to it, you select text with your mouse, and then delete with you backspace key. What if there was a better way? Something that would require a bit less jumping around interfaces? What if there was a better and faster way?

VIM is a text editor that completely discards the mouse, and allows you to double your productivity while editing code or text. 

VIM is famously know to be very hard to learn, but insanely productive once you do. 

<br>
<center>
<img src="{static}/images/vim_02.png" alt="VIM illustration" style="max-width:70%;">
</center>

So why the hell would you even use it?

## Why would you use VIM?

I was once the guy that had no clue how to quit VIM. "You need to do what to quit this?". I still remember going into my crontab and using `nano` to "edit" all my files. I had heard about these crazy people that use terminal based text editors like "vim" and "emacs". 

Today I own a VIM sweater. 
<br>
<center>
<img src="{static}/images/vim_03.png" alt="VIM Sweater" style="">
</center>

I didn't start using VIM because there was X number of reasons to switch to it. I simply wanted to play around with something other people talked about online, and I fell in love. Now that I HAVE switched to it, I can definitely recommend it for the following reasons:

- __It works on all machines.__ Whether you are on Linux or MacOS, it comes with VIM straight out of the box. Simply go to your terminal and type `vi`. 
- __It's fast.__ VIM uses something called modal editing, that makes editing and writing code (and text) much faster. You use commands such as hitting the `CI"` keys, to change the inside of a quote! Warning, VIM cheat sheets are [scary.](https://xianblog.wordpress.com/2015/03/18/the-vim-cheat-sheet/) 
- __You can make it your own.__ VIM allows you to completely customize how it behaves and how it looks. Don't like a key combo? Remap it! Don't like a certain behavior? Turn it off!

## General VIM Setup

<center>
<img src="{static}/images/vim_04.png" alt="VIM Screenshot 1" style="">
</center>

My favorite color scheme is [badwolf](https://github.com/sjl/badwolf), mainly for its Python highlighting. The markdown also doesn't look bad. The `html` though, could definitely be better. 

For fonts, I have been currently changing the font to [JetBrains Mono](https://www.jetbrains.com/lp/mono/) wherever I can.

When I am on my MacBook, I use [iTerm2](https://www.iterm2.com/) and run VIM straight from it. On Linux, the same, no need to configure anything, I just fire [Kitty](https://sw.kovidgoyal.net/kitty/), and run VIM from there. 

On Windows, I normally just run [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) with an Ubuntu Virtual Machine. Which allows me to have a relatively fast Linux machine inside Windows. *Note: If you go this route, definitely upgrade to [WSL 2](https://docs.microsoft.com/en-us/windows/wsl/wsl2-index).*


## VIM for Python development

I use some specific plugins (with [vim-plug](https://github.com/junegunn/vim-plug)) for making Python development easier. I know there are some even better ones, but I found that these strike a good balance: 

- [vim-polyglot](https://github.com/sheerun/vim-polyglot): Offers better syntax highlighting than basic VIM. 
- [black](https://github.com/psf/black/blob/master/plugin/black.vim): When writing code, I just `:Black` and it automatically makes my code pretty again. 
- [auto-pairs](https://github.com/jiangmiao/auto-pairs): Helps me "auto-close" brackets and parenthesis. And saves me time. 
- [supertab](https://github.com/ervandew/supertab): I know VIM includes some sort of tab completion. And I also know there are things like [CoC](https://github.com/neoclide/coc.nvim) and [YouCompleteMe](https://github.com/ycm-core/YouCompleteMe) out there. But hey, I just don't want to write that long variable's name. 

Great, let's see that `.vimrc`

## VIM for Markdown 

I also like using VIM for most of my markdown editing. Either it's some documentation, or even my notes (I use [Joplin](https://joplinapp.org/) to write down my notes and thoughts). Mainly because of its folding capabilities, I use [vim-markown](https://github.com/plasticboy/vim-markdown)

Great, let's see that `.vimrc`

## My `.vimrc`

Almost every line here is commented. My advice: don't copy it. Built your own from scratch, and make sure you understand every line and what it does!


```vim
filetype indent on                  " load filetype-specific indent files
syntax enable                       " enable syntax highlighting

set wildmenu                        " visual autocomplete for command menu
set showmatch                       " highlight matching !!important!!
set tabstop=4                       " number of visual spaces per tab
set softtabstop=4                   " number of spaces in tab while editing
set shiftwidth=4                    " when indenting with >, user 4 spaces width
set expandtab 	                    " tabs are spaces
set number                          " show line numbers
set showcmd                         " show command in bottom bar
set cursorline                      " highlight current line
set mouse=a                         " mouse support?                        
set vb t_vb=                        " no visual bell & flash

call plug#begin('~/.vim/plugged')       " vim-plug plugins will be downloaded there
Plug 'sjl/badwolf'                      " colorscheme
Plug 'vim-airline/vim-airline'          " nice colored bar the the bottom of the file 
Plug 'tpope/vim-fugitive'               " git versioning and bar 
Plug 'sheerun/vim-polyglot'             " syntax highlightning for different languages
Plug 'ervandew/supertab'                " tab autocomplete
Plug 'jiangmiao/auto-pairs'             " auto close brackets
Plug 'psf/black', {'tag': '19.10b0'}    " Black formatting
Plug 'plasticboy/vim-markdown'          " Markdown folding 
Plug 'ctrlpvim/ctrlp.vim'               " Allows for quick searching of files
call plug#end()                         " vim-plugs should not be declared below this.

colorscheme badwolf                     " set the colorscheme

" Configuration for vim-markdown plugin
autocmd FileType markdown let g:vim_markdown_new_list_item_indent = 0

" Because we dont want to screw with PEP 8
autocmd FileType python let g:black_linelength = 79         " max file length

" Configuration for ctrlp.vim plugin
autocmd VimEnter let g:ctrlp_working_path_mode = 'r'        " recursive
autocmd VimEnter let g:ctrlp_max_depth = 5                  " max directory depth
autocmd VimEnter let g:ctrlp_max_files = 100                " max files to parse
set wildignore+=*/tmp/*,*.so,*.swp,*.zip,*/env/*,*/venv/*   " Ignore directories
```
