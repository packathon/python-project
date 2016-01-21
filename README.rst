===================
Örnek Python Pakedi
===================

Nelere ihtiyacınız var?
-----------------------

* Herhangi bir GNU/Linux dağıtımı ya da OS X. Windows kullanıyorsanız Google en
  yakın dostunuz.
* Python 3.4 veya üzeri
* pip (Güncel Python versiyonlarıyla beraber geliyor, ayrıca kurmanıza gerek
  yok)
* setuptools (pip ile beraber geliyor, ayrıca kurmanıza gerek yok)
* [PyPI (Python Package Index)](https://pypi.python.org/pypi) hesabı
* [Test PyPI](https://testpypi.python.org/pypi) hesabı (Pakedimizi yayınlamadan
  önce burada test edeceğiz)

.. TODO: ^^ markup markdown

Dosya yapısı
------------

:requirements/requirements.txt: Pakedinizi yazarken kullandığınız üçüncü parti
    paketlerin listesi.
:requirements/dev-requirements.txt: ``requirements.txt``'den farkı pakedinizin
    kurulabilir olması için bu paketlerin zorunlu olmaması. Örneğin, testleri
    çalıştırmak ya da belgelerini HTML'e çevirmek için gereken şeyleri burada
    belirtmelisiniz.
:Makefile: Sık kullanılan komutları sürekli tekrar etmemek için kullanacağız.
    Şu anki komutlar:

    * ``make release``: Pakedimizin yeni versiyonunu yayınlamak için kullanacağız.
    * ``make test-release``: ``make release`` ile aynı işi Test PyPI üzerinde yapar.
    * ``make register``: Pakedinizin ilk versiyonunu yüklemeden önce adını kayıt etmek için kullanılacak.
    * ``make test-register``: Pakedinizi Test PyPI'da kayıt eder.
:setup.py: ``pip install requests`` dediğiniz pip'in requests'i yüklemek için
    kullandığı dosya. Pakedimizin adı, versiyonu, neleri içerdiği gibi şeyleri
    burada belirteceğiz.
:MANIFEST.in: Template, README, lisans dosyaları vb. gibi Python modulü olmayan
    içerikleri burada belirtiyoruz.
:docs/: Pakedimizin belgeleri bu klasör içinde olacak. Neredeyse her Python
    projesinde olduğu gibi biz de [Sphinx](http://www.sphinx-doc.org/en/stable/)
    kullanacağız.
:hello/: Pakedimizin içeriği.

``.pypirc`` ayar dosyası
------------------------

Pakedimizi PyPI'a yüklerken PyPI kullanıcı bilgilerimizi buraya gireceğiz.
Varsayılan olarak dosya ``$HOME`` dizi altında olmalı.

Örnek
~~~~~

.. code-block:: ini

    [distutils]
    index-servers =
        pypi
        test

    [test]
    repository = https://testpypi.python.org/pypi
    username = <TESTPYPI_KULLANICI_ADINIZ>
    password = <TESTPYPI_PAROLANIZ>

    [pypi]
    repository = http://pypi.python.org/pypi
    username = <PYPI_KULLANICI_ADINIZ>
    password = <PYPI_PAROLANIZ>


Geliştirme ortamının kurulması
------------------------------

Önce projemizin olduğu dizine girip virtualenv oluşturuyoruz::

    $ python3.4 -m venv venv

virtualenv'ı aktifleştiriyoruz::

    $ . venv/bin/activate

Bu aşamadan sonra, konsolda ``$`` yerine ``(venv) $`` görmelisiniz.

Pakedimizi kuruyoruz::

    $ pip install -e .

Bu adım aynı zamanda ``requirements/requirements.txt`` içinde belirttiğimiz
bağımlılıkları da kuracak. Ancak belgelerimizi HTML'e çevirmek için Sphinx'e
ihtiyacımız var::

    $ pip install -r requirements/dev-requirements.txt

.. TODO: -e nedir ne değildir anlat

Testleri çalıştırıyoruz::

    $ python setup.py test


Test PyPI'a paket yüklemek
--------------------------

.. TODO


Sık kullanılan komutlar
-----------------------

* Belgelerinizi HTML formatına çevirmek için: ``make -C docs html``
