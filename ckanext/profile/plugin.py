import ckan.plugins as plugins

from repoze.profile.profiler import AccumulatingProfileMiddleware

class ProfilePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IMiddleware, inherit=True)

    def make_middleware(self, app, config):
        #Profile the app
        app = AccumulatingProfileMiddleware(
            app,
            log_filename='profiling.log',
            cachegrind_filename='cachegrind.out',
            discard_first_request=True,
            flush_at_shutdown=False,
            path='/__profile__'
        )
        return app
