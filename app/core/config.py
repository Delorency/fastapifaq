import os

from pydantic_settings import BaseSettings

from dotenv import load_dotenv

load_dotenv()

class ProjectConfig(BaseSettings):
	datetime_format:str = "%Y-%m-%dT%H:%M:%S"
	date_format:str = "%Y-%m-%d"

	project_name:str = os.getenv('PROJECT_NAME', 'faq project')
	project_path:str = os.getenv('PROJECT_PATH')
	cfg:str
	for cfg in [project_name, project_path]:
		if cfg is None:
			raise Exception('Parsing project config error')


class ServerConfig(BaseSettings):
	host:str = os.getenv('HOST', 'localhost')
	port:str = os.getenv('PORT', '8080')


class DBConfig(BaseSettings):
	db_host:str = os.getenv('DB_HOST')
	db_port:str = os.getenv('DB_PORT')
	db_name:str = os.getenv('DB_NAME')
	db_user:str = os.getenv('DB_USER')
	db_pass:str = os.getenv('DB_PASS')
	cfg:str
	for cfg in [db_host, db_port, db_name, db_user, db_pass]:
		if cfg is None:
			raise Exception('Parsing db config error')

	database_uri_format:str = "postgresql://{user}:{password}@{host}:{port}/{name}"
	database_uri:str = database_uri_format.format(
		user=db_user,
		password=db_pass,
		host=db_host,
		port=db_port,
		name=db_name,
	)


class LoggerConfig(BaseSettings):
	logsdir:str = os.getenv('LOGSDIR')
	apilogfilename:str = os.getenv('APILOGFILENAME')
	dblogfilename:str = os.getenv('DBLOGFILENAME')
	cfg:str
	for cfg in [logsdir, apilogfilename, dblogfilename]:
		if cfg is None:
			raise Exception('Parsing logger config error')
	

class Configs(BaseSettings):
	projectcfg:ProjectConfig = ProjectConfig()
	servercfg:ServerConfig = ServerConfig()
	dbcfg:DBConfig = DBConfig()
	logcfg:LoggerConfig = LoggerConfig()


configs = Configs()