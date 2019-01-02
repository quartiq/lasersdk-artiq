ARTIQ controller for TOPTICA Laser SDK
======================================

.. image:: https://gitlab.com/quartiq/lasersdk-artiq/badges/master/pipeline.svg
    :target: https://gitlab.com/quartiq/lasersdk-artiq/commits/master
    :alt: CI/CD Pipeline Status

.. image:: https://anaconda.org/quartiq/lasersdk-artiq/badges/installer/conda.svg
    :target: https://anaconda.org/quartiq/lasersdk-artiq

Uses https://github.com/quartiq/lasersdk

Example: ::

    aqctl_laser -d 10.0.16.236
    artiq_rpctool localhost 3272 call get '"system-label"' '"str"'
