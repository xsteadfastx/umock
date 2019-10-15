umock
=====

`umock` is a lightwight mocking tool. Mostly developed for [micropython](https://micropython.org/) or its awesome fork [pycopy](https://github.com/pfalcon/pycopy).

Its usefull with [unittest](https://github.com/pfalcon/pycopy-lib/tree/master/unittest) your programm or to mock out any hardware interaction.

Its far from complete...

## Installing
### upip

    import upip
    upip.install("umock")


### manual
Just copy the `src/umock` folder to your `sys.path` and import it.

## Example

    from umock import MonkeyPatch, Mock

    mock_zack = Mock()
    mock_zack.return_value = "bumm"

    with MonkeyPatch(foo, "zack", mock_foo):
        print(foo.zack(1, 2))

    # you can check its call args list
    assert mock_zack.calls == [(1, 2)]
    # check how often it got called
    assert len(mock_zack.calls) == 1
