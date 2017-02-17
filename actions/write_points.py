import influxdb

from st2forge.packs import actions


class WritePointsAction(actions.Action):
    def __init__(self, config, action_service=None, logger=None):
        super(WritePointsAction, self).__init__(
            config=config,
            action_service=action_service,
            logger=logger
        )

        self.logger.debug('Instantiating WritePointsAction...')

        self.hosts = self.config.get('hosts', ['localhost'])

        if not isinstance(self.hosts, list):
            raise ValueError('The parameter "hosts" is not type of list.')

        self.port = self.config.get('port', 8086)

        if not isinstance(self.port, int):
            raise ValueError('The parameter "port" is not type of int.')

        self.username = self.config.get('username', None)
        self.password = self.config.get('password', None)

    def connect(self, database):
        options = {'database': database}

        if len(self.hosts) > 1:
            client_cls = influxdb.InfluxDBClusterClient
            options['hosts'] = [(host, self.port) for host in self.hosts]
        else:
            client_cls = influxdb.InfluxDBClient
            options['host'] = self.hosts[0]

        if self.username:
            options['username'] = self.username

        if self.password:
            options['password'] = self.password

        return client_cls(**options)

    def run(self, database, data):
        client = self.connect(database)
        client.create_database(database)
        client.write_points(data)
