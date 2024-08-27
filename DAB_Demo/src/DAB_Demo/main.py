from pyspark.sql import SparkSession, DataFrame
from DAB_Demo.src.DAB_Demo.hello_world import hello_world
from DAB_Demo.src.DAB_Demo.goodbye_world import goodbye_world

def main():
  hello_world()
  goodbye_world()

if __name__ == '__main__':
  main()
