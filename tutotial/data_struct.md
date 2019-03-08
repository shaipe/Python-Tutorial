Python数据结构
===

### Python 中的数据结构与MongoDb中数据结构对比


Python Type|BSON Type|	Supported Direction
--|--|--|
None|	null|	both
bool|	boolean|	both
int [1]	|int32 / int64	|py -> bson
long	||int64	|py -> bson
bson.int64.Int64|	int64|	both
float|	number (real)|	both
string	|string	|py -> bson
unicode	|string|	both
list|	array|	both
dict / SON	|object|	both
datetime.datetime [2] [3]	|date	|both
bson.regex.Regex	|regex	|both
compiled |re [4]	regex	|py -> bson
bson.binary.Binary	|binary	|both
bson.objectid.ObjectId	|oid	|both
bson.dbref.DBRef|	dbref|	both
None	|undefined	|bson -> py
unicode	|code|	bson -> py
bson.code.Code	|code	|py -> bson
unicode	|symbol	|bson -> py
bytes (Python 3) [5]|	binary|	both

