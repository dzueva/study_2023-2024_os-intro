---
## Front matter
title: "Отчёт по лабораторной работе №1"
subtitle: "Дисциплина: Операционные Cистемы"
author: "Зуева Дарья Тимуровна, НПМбв-01-20"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Целью данной работы является приобретение практических навыков установки операционной системы на виртуальную машину, настройки минимально необходимых для дальнейшей работы сервисов.

# Задание

1. Установить VirtualBox. Установить новую виртуальную машину. Загрузить образ.
2. Установить операционную систему и произвести первичные настройки.
3. Обновить все пакеты.
4. Установить программы для удобства работы в консоли.
5. Настроить автоматическое обновление.
6. Отключить SELinux.
7. Установить драйверы для VirtualBox.
8. Настроить клавиатуру.
9. Установить имя пользователя.
10. Подключить общую папку.
11. Установка pandoc.
12. Установка texlive.

# Выполнение лабораторной работы

### 1. Установка VirtualBox и виртуальной системы. Загрузка образа.
Так как работа ведется на Linux Ubuntu, устанавливаю VirtualBox с помощью `sudo apt install virtualbox`.
![Установка VirtualBox](image/img01.png){#fig:001 width=70%}
![Открытие Oracle VM](image/img02.png){#fig:001 width=70%}
Можно заметить, что в менеджере уже есть две виртуальные машины. Данные виртуальные машины не относятся к лабораторной работе и использоваться не будут.
С помощью GUI создаю новую виртуальную машину, Linux, Fedora(64-bit).
![Создание виртуалки](image/img03.png){#fig:001 width=70%}
Параметры моей виртуальной машины следующие:
![Параметры виртуалки](image/img04.png){#fig:001 width=70%}
Включаю поддержку UEFI:
![Включение поддержки UEFI](image/img05.png){#fig:001 width=70%}
Включаю общий буфер обмена и перетаскивание объектов между хостом и гостевой ОС:
![Включение копирования](image/img06.png){#fig:001 width=70%}

### 2. Установка операционной системы и первичная настройка
Скачиваю образ Fedora Sway Spin 40 с https://fedoraproject.org/spins/sway/download.
![Использование Fedora Sway](image/img07.png){#fig:001 width=70%}
Запускаю ОС через режим Troubleshooting и, после успешного результата, устанавливаю Fedora 40 с помощью Anaconda.
![Anaconda](image/img08.png){#fig:001 width=70%}
Корректирую настройки (язык интерфейса, имена и пароли для учетных записей, сетевое имя и т.д.).
![Anaconda. Настройки](image/img09.png){#fig:001 width=70%}
Запускаю установку:
![Установка Fedora 40](image/img10.png){#fig:001 width=70%}
После всех проделанных манипуляций делаю снапшот, выключаю машину и включаю заново, в уже загруженный образ. Машина грузится в настроенную ОС и первым делом показывает начальный экран с просьбой ввода данных пользователя.
![Начальный экран](image/img11.png){#fig:001 width=70%}
Перехожу в терминал и переключаюсь на супер-пользователя:
![Терминал. Супер-пользователь](image/img12.png){#fig:001 width=70%}

### 3. Обновление пакетов
В терминале обновляю все пакеты командой `dnf -y update`.
![Терминал. Обновление пакетов](image/img13.png){#fig:001 width=70%}

### 4. Повышение комфорта работы
Запускаю команду `dnf -y install tmux mc`:
![Терминал. Удобство в консоли](image/img14.png){#fig:001 width=70%}
### 5. Настройка автоматического обновления
Устанавливаю программное обеспечение для автоматического обновления командой `dnf install dnf-automatic`:
![Терминал. Автоматическое обновление](image/img15.png){#fig:001 width=70%}
Смотрю конфигурацию `/etc/dnf/automatic.conf`. Меня в ней все устраивает, поэтому оставляю ее как она уже есть. Запускаю таймер:
![Терминал. Запуск таймера](image/img16.png){#fig:001 width=70%}

### 6. Отключение SELinux
Открываю `/etc/selinux/config` (я использую утилиту `nano`) и заменяю `SELINUX=enforcing` на `SELINUX=permissive`.
![Терминал. Отключение SELinux](image/img17.png){#fig:001 width=70%}

Перезагружаю виртуальную машину командой `reboot`.

### 7. Установка драйверов для VirtualBox
После перезагрузки заново захожу в систему и открываю терминал. Запускаю терминальный мультиплексор `tmux` и переключаюсь на супер-пользователя с помощью `sudo -i`.
Устанавливаю средства разработки командой `dnf -y group install "Development Tools"`:
![Терминал. Установка средств разработки](image/img18.png){#fig:001 width=70%}
Устанавливаю пакет DKMS (для обновления индивидуальных модулей ядра без изменения всего ядра целиком):
![Терминал. Установка DKMS](image/img19.png){#fig:001 width=70%}

Перезагружаю виртуальную машину с помощью `reboot`.

### 8. Настройка раскладки клавиатуры
На виртуальной машине создаю конфигурационный файл `~/.config/sway/config.d/95-system-keyboard-config.conf` и редактируем его:
![Терминал. Конфиг клавиатуры](image/img20.png){#fig:001 width=70%}
Переключаюсь в супер-пользователя и редактирую следующий конфигурационный файл `/etc/X11/xorg.conf.d/00-keyboard.conf`:
![Терминал. X11 Конфиг клавиатуры](image/img21.png){#fig:001 width=70%}

Перезагружаю виртуальную машину с помощью `reboot`.

### 9. Установка имени пользователя и названия хоста
После перезагрузки снова захожу в систему и открываю терминал. Переключаюсь в супер-пользователя.
Создаю пользователя (dzueva), задаю для него пароль и устанавливаю имя хоста. Проверяю:
![Терминал. Установка имени пользователя](image/img23.png){#fig:001 width=70%}

### 10. Подключение общей папки
Внутри виртуальной машины добавлю своего пользователя в группу `vboxsf`:
![Терминал. Добавление пользователя](image/img24.png){#fig:001 width=70%}
Останавливаю виртуальную машину и подключаю разделяемую папку в хостовой системе:
![Подключение разделяемой папки](image/img25.png){#fig:001 width=70%}

### 11. Установка и настройка pandoc
Устанавливаю средство `pandoc` для работы с языком разметки Markdown:
![Терминал. Установка pandoc](image/img22.png){#fig:001 width=70%}
Таким же образом устанавливаю `pandoc-crossref`.

# Выводы

По итогам проделанной работы были приобретены навыки установки и настройки операционной системы на виртуальную машину, а так же были приобретены навыки настройки минимально необходимых для дальнейше работы сервисов.
# Список литературы{.unnumbered}
[Руководство к лабораторной работе](https://esystem.rudn.ru/mod/page/view.php?id=1103905)
::: {#refs}
:::
