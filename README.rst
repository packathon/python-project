===================
Örnek Python Paketi
===================

.. image:: https://travis-ci.org/packathon/python-project.svg?branch=master
    :target: https://travis-ci.org/packathon/python-project

* Bu belge, en az eforla ilk Python paketinizi standart Python kütüphanesinde
  yer alan araçları kullanarak geliştirmeniz ve PyPI üzerinde yayınlamanız
  için ihtiyacınız olan şeyleri listelemektedir. Örneğin, testler için
  pytest_ ya da nose_ yerine standart kütüphanede yer alan unittest_
  paketini kullanacağız ve Wheel_ formatına değinmeyeceğiz.
* Kod içerisinde çeşitli yerlerde daha fazla bilgi vermek için yorumlar
  eklendi.
* En güncel bilgiler için resmi Python belgelerine göz atabilirsiniz:
  https://packaging.python.org/en/latest/

.. _pytest: http://pytest.org/latest/
.. _nose: https://nose.readthedocs.org/en/latest/
.. _unittest: https://docs.python.org/3/library/unittest.html
.. _Wheel: https://wheel.readthedocs.org/en/latest/


Nelere ihtiyacınız var?
-----------------------

* Herhangi bir GNU/Linux dağıtımı ya da OS X. Windows kullanıyorsanız Google en
  yakın dostunuz.
* Python 3.4 veya üzeri
* pip (Güncel Python versiyonlarıyla beraber geliyor, ayrıca kurmanıza gerek
  yok)
* setuptools (pip ile beraber geliyor, ayrıca kurmanıza gerek yok)
* PyPI_ (Python Package Index) hesabı
* `Test PyPI`_ hesabı (Paketimizi yayınlamadan önce burada test edeceğiz)

.. _PyPI: https://pypi.python.org/pypi
.. _`Test PyPI`: https://testpypi.python.org/pypi


Dosya yapısı
------------

:requirements/requirements.txt: Paketinizi yazarken kullandığınız üçüncü parti
    paketlerin listesi.
:requirements/dev-requirements.txt: ``requirements.txt``'den farkı paketinizin
    kurulabilir olması için bu paketlerin zorunlu olmaması. Örneğin, testleri
    çalıştırmak ya da belgelerini HTML'e çevirmek için gereken şeyleri burada
    belirtmelisiniz.
:Makefile: Sık kullanılan komutları sürekli tekrar etmemek için kullanacağız.
    Şu anki komutlar:

    * ``make release``: Paketimizin yeni versiyonunu yayınlamak için kullanacağız.
    * ``make test-release``: ``make release`` ile aynı işi Test PyPI üzerinde yapar.
    * ``make register``: Paketinizin ilk versiyonunu yüklemeden önce adını kayıt etmek için kullanılacak.
    * ``make test-register``: Paketinizi Test PyPI'da kayıt eder.
:setup.py: ``pip install requests`` dediğiniz pip'in requests'i yüklemek için
    kullandığı dosya. Paketimizin adı, versiyonu, neleri içerdiği gibi şeyleri
    burada belirteceğiz.
:MANIFEST.in: Template, README, lisans dosyaları vb. gibi Python modulü olmayan
    içerikleri burada belirtiyoruz.
:docs/: Paketimizin belgeleri bu klasör içinde olacak. Neredeyse her Python
    projesinde olduğu gibi biz de [Sphinx](http://www.sphinx-doc.org/en/stable/)
    kullanacağız.
:hello/: Paketimizin içeriği.


``.pypirc`` ayar dosyası
------------------------

Paketimizi PyPI'a yüklerken PyPI kullanıcı bilgilerimizi buraya gireceğiz.
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

Paketimizi kuruyoruz::

    $ pip install -e .

Bu adım aynı zamanda ``requirements/requirements.txt`` içinde belirttiğimiz
bağımlılıkları da kuracak. Ancak belgelerimizi HTML'e çevirmek için Sphinx'e
ihtiyacımız var::

    $ pip install -r requirements/dev-requirements.txt

.. TODO: -e nedir ne değildir anlat

Testleri çalıştırıyoruz::

    $ python -m unittest discover


Test PyPI'a paket yüklemek
--------------------------

Paketimizi yayınlamadan önce paket adı gibi meta verileri PyPI'a göndermemiz
gerekiyor. Ama önce her şeyin yolunda olup olmadığını kontrol için Test PyPI'ı
kullanalım::

    $ make test-register
    # ya da
    $ python setup.py sdist register -r test

Paketimizi Test PyPI'a yüklemek için ``test-release`` komutunu kullanacağız::

    $ make test-release
    # ya da
    $ python setup.py sdist upload -r test

Eğer her şey yolunda gitti ise, şimdi yeni bir virtualenv yaratarak paketimizi
kuralım::

    # kullandığımız virtualenv'den çıkalım
    $ deactivate
    # yeni bir virtualenv oluşturalım
    $ python -m venv test-venv
    $ . test-venv/bin/activate

Şimdi paketimizi Test PyPI'dan kurup kontrol edelim::

    $ pip install -i https://testpypi.python.org/pypi <PAKET_ADI>
    $ python -c "import hello; hello.say_hello('BYK')"
    Hello, BYK!

Eğer her şey beklediğiniz gibiyse, aynı adımları komutlardan ``test-`` kısmını
kaldırarak takip edip ilk Python paketinizi PyPI_ üzerinde yayımlayabilirsiniz.


Sık kullanılan komutlar
-----------------------

* Belgelerinizi HTML formatına çevirmek için: ``make -C docs html``
* Testleri çalıştırmak için: ``python -m unittest discover`` (basit testler
  için direkt olarak test dosyasını da çalıştırabilirsiniz:
  ``python tests/test_hello.py``)
