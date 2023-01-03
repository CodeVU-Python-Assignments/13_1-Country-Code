import geo_country_codes

input = ['Kansas City, MO', 'Brazil', 'Atlantic Ocean']

def test_print_country_code_from_geocoding_given_kansas_city_prints_us(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:input.pop(0))
    geo_country_codes.print_country_code_from_geocoding()
    out, err = capfd.readouterr()
    assert 'US' in out

def test_print_country_code_from_geocoding_given_brazil_prints_br(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:input.pop(0))
    geo_country_codes.print_country_code_from_geocoding()
    out, err = capfd.readouterr()
    assert 'BR' in out

def test_print_country_code_from_geocoding_given_ocean_prints_not_found(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:input.pop(0))
    geo_country_codes.print_country_code_from_geocoding()
    out, err = capfd.readouterr()
    assert 'No country code found' in out or 'No country code found' in err
    
