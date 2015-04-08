import DS from 'ember-data';

export default DS.RESTAdapter.extend({
  coalesceFindRequests: true,
  namespace: 'api'
});

//test!!!
// I see you! :) :)

// http://virtualenvwrapper.readthedocs.org/en/latest/index.html#introduction


// sudo pip install virtualenvwrapper

// export WORKON_HOME=~/.virtualenvs
// source /usr/local/bin/virtualenvwrapper.sh

// mkvirtualenv wibi
// pip freeze
// workon wibi
// pip freeze
// pip install -r requirements.txt