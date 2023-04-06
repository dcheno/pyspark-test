from pyspark.sql import SparkSession

from edit import trainers_by_type


def main() -> None:
    spark = SparkSession.builder.master("local[1]").appName("SparkTest").getOrCreate()

    pokemon = spark.read.csv("data/pokemon.csv", header=True)
    trainers = spark.read.csv("data/trainers.csv", header=True)

    df = trainers_by_type(pokemon, trainers)

    df.show()

    spark.stop()


if __name__ == "__main__":
    main()
