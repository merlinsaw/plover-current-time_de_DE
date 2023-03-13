import datetime
import locale

def meta(ctx, cmdline):
    action = ctx.new_action()
    action.text = time(cmdline)
    return action

def time(formatting):
    fmt, *set_locale = formatting.split('>>')

    # save current locale to restore it later
    current_locale = locale.getlocale()[0]

    if set_locale:
        if set_locale[0] == 'de_DE':
            locale.setlocale(locale.LC_ALL, 'de_DE')
        elif set_locale[0] == 'en_GB':
            locale.setlocale(locale.LC_ALL, 'en_GB')
        else:
            locale.setlocale(locale.LC_ALL, set_locale[0])
            try:
                print("Try setting locale to " + set_locale[0])
                locale.setlocale(locale.LC_ALL, set_locale[0])
            except locale.Error:
                print("Locale " + set_locale[0] + " not found")
                print("Current locale is " + current_locale)
                print(locale.getlocale())
                alllocale = locale.locale_alias
                for k in alllocale.keys():
                    print('locale[%s] %s' % (k, alllocale[k]))
                return
            print(set_locale[0])
    else:
        print(current_locale + " is the current locale")
        print(locale.getlocale())

    now = datetime.datetime.now()
    formatted = now.strftime(fmt)

    # restore current locale
    locale.setlocale(locale.LC_ALL, current_locale)

    return(formatted)
