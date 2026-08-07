default persistent.oimon_mod_detected = True
default persistent.oimon_mod_enabled = True

init 105 python:
    def oimon_mod_add_option(func):
        def func_extension():
            options = func()
            options.append( ("Enable Smol Tits Mod", "oimon_mod_enabled", persistent))
            return options
        return func_extension

    mod_options = oimon_mod_add_option(mod_options)