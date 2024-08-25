#protoc --proto_path=$SRC_DIR --python_out=$DST_DIR  --grpc_python_out=$DST_DIR  $SRC_DIR/yourprotifle.proto
python -m grpc_tools.protoc -Igenerated=protos   --python_out=. --grpc_python_out=.  protos/weatherservice.proto
