# Посібник з Інструментів для додатків NVDA

Цей додаток намагається бути набором інструментів для наших встановлених та невстановлених додатків.

У різних ситуаціях ми намагаємося бути якнайшвидшими, надаючи можливість виконувати дії з нашими додатками масово, а не по одному, як у менеджері додатків.

Вже додані можливості будуть поліпшені в різних версіях, а також додані нові функції.

Цей додаток можна запустити в меню Інструменти / Інструменти для додатків NVDA.

Для швидкого запуску додатка не призначено клавіатурної команди.

Жест можна додати з меню Параметри/Жести вводу... та знайти категорію «Інструменти для додатків NVDA».

## Відмова від відповідальності

Кінцевий користувач несе повну відповідальність за використання додатка.

Ми намагаємося зробити все якомога надійнішим, але проблеми завжди можуть виникнути, і автор додатка не несе відповідальності за будь-які проблеми, що виникають при використанні цього додатка.

# Загальний опис

Додаток розділено на 3 розділи.

* 1-ий розділ: Список, у якому ми можемо вибрати категорію, яку хочемо використати. Саме на ньому зосереджується увага щоразу, коли ми активовуємо додаток.

У цьому списку ми будемо переміщуватись за допомогою стрілок вгору і вниз.

* 2-ий розділ: Область, яка включає вміст категорії, яку ми обрали.

Ця область може змінюватись в залежності від категорії. Опис категорій — нижче.

Ми можемо отримувати доступ до категорій за допомогою клавіші tab.

* 3-й розділ: Цей розділ містить вікно редагування, яке активується при виконанні будь-якої дії, надаючи користувачеві інформацію про те, що відбувається. Він також інформуватиме користувача за допомогою індикатора виконання про перебіг усіх дій.

Він також включає кнопки, які дозволять нам взаємодіяти в залежності від того, що сталося при виконанні дії, наприклад, кнопку «Закрити», яка закриє додаток.

Поки не відбувається жодних дій, плагін можна закрити за допомогою Escape, Alt+F4 або, перейшовши клавішею tab  до кнопки «Закрити».

## Пакувальник додатків

Якщо ми виберемо цю категорію, нам буде надано список усіх встановлених додатків, незалежно від того, увімкнені вони, вимкнені або не підтримуються.

Ми також можемо швидко перейти до нього за допомогою Alt+L, у цьому списку можна вибрати пробілом усі додатки, які ми хочемо вибрати для створення резервної копії у каталозі, який ми вкажемо.

Кожен додаток буде згенеровано зі своїм ім'ям та версією, а також ідентифікаційним тегом «_gen», ці згенеровані додатки можуть бути встановлені за допомогою NVDA без будь-яких проблем.

Якщо ми натиснемо tab, то потрапимо на кнопку «Вибрати», або ж ми можемо швидко отримати доступ до неї за допомогою Alt+S. Якщо ми натиснемо на цю кнопку, то з’явиться меню швидкого вибору або скасування вибору всіх додатків.

Якщо ми знову натиснемо tab, то потрапимо на кнопку «Згенерувати», швидкий доступ до якої можна отримати комбінацією Alt+G. Якщо ми натиснемо цю кнопку і ми маємо хоча б один вибраний додаток, то відкриється вікно для вибору папки, куди ми хочемо зберегти обраний додаток чи обрані додатки.

Після вибору папки і натискання кнопки «Гаразд», почнеться створення додатків. Фокус залишиться в полі, доступному лише для читання, де з’явиться інформація разом з індикатором перебігу, яка дозволяє дізнатися відсоток виконання. Кнопка закриття, а також решта інтерфейсу будуть недоступними, допоки не завершиться процес генерації додатків.

Після завершення дії він повідомить нам, чи все було успішно, а чи виникли якісь проблеми, і якщо ми натиснемо tab, то зможемо обрати кнопки «Гаразд» (Alt+A), «Скасувати» (Alt+C) або закрити інтерфейс.

Залежно від того, як було виконано дію, з'являться кнопки «Гаразд» і «Скасувати».

Для генерації додатків необхідно вибрати щонайменше один, в іншому разі ми отримаємо попередження.

## Мультивстановлювач

Ця категорія дозволить нам вибрати папку з додатками, і ми зможемо встановити їх всіх відразу.

Коли ми увійдемо в цю категорію, то побачимо кнопку вибору папки з додатками для встановлення... її також можна активувати клавішами Alt+S. якщо ми її натиснемо, то з’явиться вікно для вибору папки з додатками.

Решта інтерфейсу в цій категорії недоступна, допоки ви не оберете папку.

Коли ми виберемо папку, фокус буде зосереджено на полі лише для читання, де ми будемо отримувати інформацію про те, що відбувається під час сканування на наявність додатків, а також отримуватимемо інформацію про індикатор перебігу.

Після завершення сканування нам повідомлять, чи були якісь проблеми та як діяти. Він прийматиме лише додатки, які відповідають API встановленої в нас NVDA, відкидаючи всі несумісні або пошкоджені додатки.

Після завершення сканування, якщо воно виявило додатки й ми натиснемо кнопку «Гаразд», буде активовано список із назвами додатків, знайдених у цій папці.

Ми можемо швидко перейти до цього списку за допомогою (Alt+L), у цьому списку ми можемо вибрати стільки додатків, скільки захочемо, позначивши їх пробілом.

Якщо ми натиснемо tab, у нас буде така сама кнопка вибору, що і в пакувальнику додатків, яку я не поясню, тому що це те саме використання.

При повторному натисканні tab або команди Alt+I ми потрапимо на кнопку «Встановити».

Якщо у нас вибрано хоча б один додаток і ми натиснемо цю кнопку, то встановлення додатка (або додатків) буде здійснено по одному або по кілька без відображення класичного вікна встановлення додатків в NVDA, цим ми прискорюємо встановлення додатків.

Цей крок також має такі захисти, як перевірка API, що додаток не пошкоджено та інші внутрішні речі NVDA. Все для того, щоб завжди намагатися досягти максимальної продуктивності нашого скрінрідера.

Коли ми натиснемо кнопку встановлення, фокус буде на полі лише для читання, де ми будемо отримувати інформацію про те, що робить додаток.

Аналогічно, після завершення роботи ми отримаємо інформацію про те, чи все пройшло успішно, або ж про невдачу встановлення чи інші помилки.
 
Залежно від того, що сталося, додаток покаже кнопку «Гаразд» або «Скасувати» поруч із кнопкою закриття.

Якщо ви побачите кнопку «Гаразд», це означає, що NVDA встановила додаток і для застосування змін їй потрібно перезапуститися, якщо ми натиснемо її, то NVDA перезапуститься і в нас будуть встановлені додатки.

Якщо ми цього не зробимо, то не зможемо використовувати додаток, допоки не перезапустимо NVDA, це захист, щоб уникнути дублювання дій.

Якщо в іншому випадку відбулися збої й відображено лише кнопку скасування, ми можемо натиснути її та повернутися до інтерфейсу для виконання інших дій.

### ПОПЕРЕДЖЕННЯ

Ця категорія реалізована для пришвидшення встановлення додатків, але зловживання таким методом встановлення може призвести до збоїв у роботі NVDA. Відповідальність за її використання лежить на користувачеві.

## Видалення додатків

Ця категорія дозволяє видаляти додатки швидко та за один раз.

Ми можемо вибрати зі списку один або кілька встановлених  додатків, позначаючи їх пробілом. Для швидкого переходу до списку можетенатиснути Alt+L.

У нас також є кнопка вибору (Alt+S), яка має таку саму функцію, як і в попередніх категоріях, і я не пояснюватиму її знову.

Натиснувши tab або комбінацію Alt+D, ми знайдемо кнопку «Видалити». Якщо ми натиснемо її і у нас вибрано один або кілька додатків, вона залишить фокус у полі для читання і повідомить нам про те, що відбувається.

Ми також отримуватимемо інформацію через індикатор виконання.

Після завершення нам повідомлять результат, і, як у категорії «Мультивстановлювач», у нас буде кнопка «Гаразд», за допомогою якої потрібно буде перезапустити NVDA або «Скасувати», якщо щось пішло не так, і кнопка «Закрити».

Пам'ятайте, що якщо ми закрили цю категорію і не звернули увагу на необхідність перезапуску, додаток не може бути використаний знову, поки NVDA не буде перезапущено.

### Попередження

Видалення додатків після натискання кнопки «Видалити» незворотне, тому варто переконатися, що ми знаємо, де взяти додатки, які ми видалили, на випадок, якщо захочемо встановити їх знову, і якщо додаток містить інформацію в каталозі додатків, її буде видалено.

Це не дуже хороша практика і NVDA не рекомендує зберігати інформацію в тому ж каталозі, де встановлено додаток, але це вирішує розробник додатка.

Тому, повторюю, використовуйте цю категорію на свій страх та ризик.

## Увімкнення/вимкнення додатків

Ця категорія дозволить нам вмикати чи вимикати одразу кілька додатків.

Якщо ми ввійдемо в цю категорію, то потрапимо до списку увімкнених додатків, який можна швидко відкрити за допомогою Alt+L. Клавішею пробіл ми можемо позначити ті додатки, які хочемо вимкнути.

Якщо у нас є вимкнені додатки, то з’явиться другий список із цими додатками, ми можемо швидко переміщатися між списками за допомогою Alt+L. У списку вимкнених додатків ми також можемо позначити пробілом ті, які хочемо увімкнути.

Ми можемо позначити додатки в обох списках, незважаючи на те, що дія буде виконана у зворотному порядку, тобто увімкнені додатки вимкнуться, а вимкнені — увімкнуться.

У цій категорії також є кнопка вибору, але з невеликою відмінністю: при натисканні на неї з'являється підменю для кожного списку, і ми можемо вибрати або скасувати вибір в обраному нами списку.

Якщо ми натиснемо tab, то знайдемо кнопку розпочати (швидкий доступ Alt+P), якщо ми натиснемо її, то фокус залишиться в полі лише для читання з повідомленням про перебіг.
, і вона повідомить про те, що вона робить.

Коли дію буде завершено, вона відбудеться так само, як у попередніх категоріях, інформуючи нас і активуючи відповідні кнопки.

Ще раз нагадую, якщо дія пройшла успішно і ми не перезапустилися, додаток не можна бути використовувати до перезапуску NVDA.

## Редагування маніфесту

У цій категорії ми зможемо змінити маніфест, щоб зробити додатки сумісними з API, потрібним NVDA. Ми зможемо змінити маніфест як встановлених додатків, як і не встановлених.

Тепер, згідно з останньою політикою NVDA і до подальших змін, щороку в першому випуску NVDA розробники повинні змінювати версію, щоб їхній маніфест відповідав версії NVDA.

Деякі розробники зроблять це відразу, іншим знадобиться деякий час, а треті просто не робитимуть цього через відмову від додатків або з будь-якої іншої причини.

В останньому випадку нам доведеться вручну змінювати властивість lastTestedNVDAVersion, а якщо у нас багато додатків, то доведеться витратити час, до того ж це завдання не для всіх користувачів, оскільки існує багато рівнів користувачів.

Також, якщо ми хочемо тестувати бета- або RC-версії, нам доведеться змінити цей параметр у маніфестах, інакше ми не зможемо встановити додаток.

NVDA — це програма для читання екрана, яка перебуває в постійному розвитку, тому часто з’являються додатки, які залишаються на узбіччі через відсутність розвитку та адаптації до змін, які NVDA привносить у свій розвиток.

Це означає, що зміна дати в маніфестах вирішує цю проблему, щоб мати можливість продовжувати використовувати додатки, які не оновлюються або розробник зволікає з їх оновленням. Але будуть додатки, які, окрім зміни маніфесту, вимагають внутрішніх змін для адаптації до нових версій, у такому разі додаток зламається і вам залишиться лише зв’язатися з його автором.

Рекомендується оновлювати додатки, які виходять зі змінами в маніфестах, навіть якщо ми змінили дату за допомогою цього інструмента, оскільки можливо, що ці додатки приносять, крім адаптації маніфесту, інші зміни, які вніс розробник.

Зайшовши в цю категорію, ми побачимо список з усіма встановленими додатками разом з їхньою версією API. Ми можемо отримати швидкий доступ до цього списку комбінацією Alt+L. У ньому ми зможемо позначити один або кілька додатків, маніфест яких хочемо змінити.

Якщо ми натиснемо tab, то потрапимо до трьох комбінованих списків:

* Виберіть основну версію: Це комбіноване поле має відповідати року версії NVDA.

* Виберіть другорядну версію: Тут достатньо залишити значення 1, але я створив чотири річні версії на випадок змін (бо може статися що завгодно).

* Редакція: У цьому комбінованому списку достатньо залишити значення 0, але про всяк випадок я помістив значення до 9.

Під час табуляції у нас знову є кнопка вибору, яка дозволить нам вибрати або скасувати вибір усіх додатків у списку.

Якщо ми знову натиснемо tab, то потрапимо на кнопку «Розпочати», або ми можемо швидко перейти до неї за допомогою Alt+P.

Якщо натиснути цю кнопку, з'явиться меню з такими параметрами:

* Розпочати встановлення, якщо ми виберемо цей параметр, розпочнеться процес зміни маніфесту встановлених додатків, які ми вибрали. Їх буде замінено тими, які ми вибрали в комбінованих списках «Основна версія», «Другорядна версія» і «Редакція».

* Опрацювати файл додатка, якщо ми виберемо цей параметр, відкриється вікно вибору файлу, де ми повинні будемо вибрати файл додатка, в якому ми хочемо змінити маніфест. Спочатку ми маємо вибрати основну, другорядну та редакційну версії, які будуть застосовані до нього.

Якщо ми вирішили змінити маніфест у файлі і процес пройшов успішно, у вихідному каталозі додатка буде згенеровано інший додаток з тим самим ім’ям, але з тегом «_gen_modify_manifest», який міститиме змінений маніфест, щоб його можна було використовувати.

За будь-якого з цих двох варіантів фокус буде залишено в полі тільки для читання, і ми будемо поінформовані про те, що відбувається.

Поведінка буде такою ж, як і в попередніх категоріях з кнопками згоди і скасування.

Пам'ятайте, що якщо ми вибираємо файл додатка, ми повинні спочатку змінити значення в комбінованих списках «Основна версія», «Другорядна версія» і «Редакція», щоб конфігурація була використана до файлу, який ми вибрали.

### Попередження

Відповідальність за використання цієї утиліти та її результати несе виключно кінцевий користувач.

## Документація додатків

Оскільки деяким людям важко знайти документацію до додатків, то у цій категорії ми зможемо звернутися до документації встановлених додатків.

У цій категорії ми знайдемо список (швидка комбінація — Alt+L), який покаже всі додатки, які мають документацію, крім тих, які з якоїсь причини не мають документації.

Натиснувши tab,  ми знайдемо кнопку «Відкрити документацію додатка» (Alt+A). Якщо ми активуємо цю кнопку, то у нашому основному браузері буде відкрито документацію вибраного додатка.

# Перекладачі й учасники:

Якщо хтось хоче допомогти з перекладами, ви можете зробити це через репозиторій додатка на Github або надіслати листа на адресу xebolax@gmail.com.
* Inglés: Traducción automatica
* Turco: umut korkmaz

# Журнал змін.
## Інформація про оновлення:

Цей додаток має такий принцип оновлень:

У цій історії перелічено лише зміни у версіях типу  major.minor. (наприклад, v3.1).

Версії major.minor.x (наприклад, v3.1.2) є оновленнями перекладу.

Зміни в додатку відображатимуться в цьому розділі з поясненням того, що саме змінилося.

Основний документ залишиться без змін як посібник для користувача.

Користувач несе відповідальність за перегляд цього розділу, щоб бути поінформованим про зміни.

## Версія 1.2.

* Виправлено серйозні помилки в резервному копіюванні.

## Версія 1.1.

* Виправлено помилки.

* Додано можливість створення й відновлення резервних копій.

Тепер у нас з'явиться новий розділ під назвою Створення/відновлення резервних копій.

Цей розділ покаже у вигляді списку доступні для рзервування варіанти.

Параметри, які можуть бути збережені в резервній копії:

* Каталоги словників (\speechDicts)
* Каталог профілів (\profiles)
* Каталог scratchpad (\scratchpad)
* Файл конфігурації автоперемикання профілю (profileTriggers.ini)
* Файл конфігурації жестів вводу (gestures.ini)
* конфігураційний файл NVDA (nvda.ini)

У списку буде показано лише ті елементи, які присутні в нашій копії NVDA, а також ті каталоги, які мають вміст.

Якщо, наприклад, каталог профілю порожній, це не дозволить вам зробити резервну копію.

Для створення резервної копії необхідно вибрати принаймні один елемент зі списку.

Якщо ми перейдемо на вкладку, то побачимо дві кнопки:

* Створити резервну копію

Якщо ми натиснемо цю кнопку, відкриється класичне вікно збереження Windows, в якому нам буде запропоновано ввести ім'я нашої резервної копії та місце, куди ми хочемо її зберегти.

Коли ми натиснемо на кнопку «Зберегти», додаток почне резервне копіювання, а в полі стану, доступному лише для читання, він повідомить нам результат, якщо все пройшло добре або були помилки.

* Відновити з резервної копії

При натисканні на цю кнопку відкриється класичне вікно Windows для відкриття файлу резервної копії, нам потрібно буде знайти його там, де ми зберегли резервну копію, і натиснути на кнопку відкрити.

Після відкриття файлу з'явиться вікно з вмістом резервної копії, в цьому вікні з'явиться список для вибору тих елементів, які ми хочемо відновити.

Якщо ми хочемо відновити, натискаємо на кнопку «Відновити» і поле стану повідомить нам, чи відновлення пройшло успішно, чи виникла проблема.

ПОПЕРЕДЖЕННЯ:

Коли ми відновлюємо елемент, який стосується NVDA, буде потрібно перезапустити NVDA, тому будь-яка дія, яку ми виконуємо в «Інструментах для додатків NVDA», призведе до перезапуску NVDA, незалежно від того, яку кнопку ми натиснемо — «прийняти», «скасувати», «закрити», escape або Alt+F4.

Якщо при відновленні декількох елементів виникає помилка, відновлюється тільки один елемент і NVDA перезапускається.

## Версія 1.0.

* Versión inicial.

Se a reescrito desde cero lo que era el antiguo Empaquetador de complementos junto a la incorporación de nuevas funciones.

El complemento cambia de nombre a Utilidades para los complementos de NVDA pero sigue manteniendo el nombre interno que maneja NVDA en (addonPackager).

Al lanzar esta versión el complemento cricricri quedara sin mantenimiento ya que este complemento ya incluye el cambio de manifiestos.
