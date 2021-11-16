demo1:
	rsync -avuz -e 'ssh -p 2121' ./ cmput274@localhost:BackUp
