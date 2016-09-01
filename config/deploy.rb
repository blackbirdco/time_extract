require 'mina/git'

set :domain, 'jam-nlp'
set :branch, 'master'

set :repository, 'git@github.com:blackbirdco/jam_nlp.git'
set :deploy_to, '/var/www/jam_nlp'

task :setup => :environment do
  queue! %[mkdir -p "#{deploy_to}/shared/log"]
  queue! %[chmod g+rx,u+rwx "#{deploy_to}/shared/log"]
  queue! %[mkdir -p "#{deploy_to}/shared/secrets"]
  queue! %[chmod g+rx,u+rwx "#{deploy_to}/shared/secrets"]
  queue! %[mkdir -p "#{deploy_to}/shared/out"]
  queue! %[chmod g+rx,u+rwx "#{deploy_to}/shared/out"]
  queue! %[mkdir -p "#{deploy_to}/shared/TreeTagger"]
  queue! %[chmod g+rx,u+rwx "#{deploy_to}/shared/TreeTagger"]
end

set :shared_paths, [
  'log',
  'secrets',
  'out',
  'TreeTagger',
]

task :logs do
  queue "tail -f #{deploy_to}/current/log/access.log"
end

task :logs_error do
  queue "tail -f #{deploy_to}/current/log/error.log"
end

desc "Deploys the current version to the server."
task :deploy => :environment do
  deploy do
    invoke :'git:clone'
    queue 'sudo pip install -r requirements.txt'
    invoke :'deploy:link_shared_paths'

    to :launch do
      queue 'supervisorctl restart jam_nlp'
    end
  end
end

