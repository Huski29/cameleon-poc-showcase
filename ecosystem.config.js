module.exports = {
  apps: [
    {
      name: 'cameleon-backend',
      script: './start_server.sh',
      cwd: '/home/xsolai/hdd/Projects/cameleon-poc-showcase/backend',
      interpreter: 'bash',
      env: {
        PYTHONUNBUFFERED: '1'
      },
      error_file: '/home/xsolai/hdd/Projects/cameleon-poc-showcase/backend/logs/pm2-error.log',
      out_file: '/home/xsolai/hdd/Projects/cameleon-poc-showcase/backend/logs/pm2-out.log',
      time: true
    },
    {
      name: 'cameleon-frontend',
      script: 'npm',
      args: 'run dev',
      cwd: '/home/xsolai/hdd/Projects/cameleon-poc-showcase/frontend',
      env: {
        PORT: '3000',
        NODE_ENV: 'development',
        NEXT_PUBLIC_API_URL: 'https://showcase.cameleon.fit'
      },
      error_file: '/home/xsolai/hdd/Projects/cameleon-poc-showcase/frontend/logs/pm2-error.log',
      out_file: '/home/xsolai/hdd/Projects/cameleon-poc-showcase/frontend/logs/pm2-out.log',
      time: true
    }
  ]
};

