%env HADOOP_HDFS_HOME=/opt/cloudera/parcels/CDH/lib/hadoop-hdfs
%env LD_LIBRARY_PATH=/opt/cloudera/parcels/CDH/lib/hadoop/lib/native:/opt/cloudera/parcels/GPLEXTRAS/lib/hadoop/lib/native:/opt/cloudera/parcels/CDH/lib64/:/usr/java/jdk1.8.0_121//jre/lib/amd64/server

!CLASSPATH=$(hadoop classpath --glob) python fully_connected_reader.py --train_dir hdfs://default/tmp/mnist

#!python fully_connected_reader.py --train_dir hdfs://cdsw-demo-4.vpc.cloudera.com:8020/tmp/data/mnist