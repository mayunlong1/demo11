import logging
import sys

message = None
str_def_fmt = '[%(asctime).19s] %(process)d:%(levelname).1s %(filename)s:%(lineno)d:%(funcName)s: %(message).50s'

logging.basicConfig(level=logging.DEBUG
                    , format=str_def_fmt
                    , datefmt="%Y:%m:%d %H:%M:%S"
                    , stream=sys.stdout)
logger = logging.getLogger(__name__)
d = logging.debug

def main():
    d("132132321231qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")


if __name__ == "__main__":
    main()

    # print(str_def_fmt)

# mat = "{:20}\t{:28}\t{:32}"
# print(mat.format("占4个长度","占8个长度", "占12长度"))
# #如果需要居中输出在宽度前面加一个^
# mat = "{:^20}\t{:^28}\t{:^32}"
# print(mat.format("占4个长度","占8个长度", "占12长度"))
