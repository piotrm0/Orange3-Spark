__author__ = 'jamh'

from Orange.widgets import widget
from pyspark.ml import clustering

from ..base.spark_ml_estimator import OWSparkEstimator


class OWSparkMLClustering(OWSparkEstimator, widget.OWWidget):
    name = "Clustering"
    description = "Clustering algorithms"
    icon = "icons/spark.png"

    module = clustering
    module_name = 'clustering'
    box_text = "Spark Clustering Algorithms"
