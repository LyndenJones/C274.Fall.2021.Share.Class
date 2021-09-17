test:
	python3 passwordvalidate.py
	python3 testwe1.py

subtest:
	make tar
	@echo "**** Currently works on the VM and in CSC 1-21. Problems on some MacOS systems."
	(cd ..; python3 submission_validator.py)

tar:
	(cd ..; tar cvf passwordvalidate.tar passwordvalidate/passwordvalidate.py passwordvalidate/README)
	gzip ../passwordvalidate.tar

clean:
# For MacOS
	-rm .DS_Store
	-rm ../passwordvalidate.tar.gz
