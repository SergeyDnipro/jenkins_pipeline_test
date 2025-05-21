pipeline {
  agent any

  environment {
    VENV_DIR = '.venv'
    SHARED_DIR = '/shared'
    ALLURE_RESULTS = 'allure-results'
    LOG_DIR = 'logs'
    DATABASE_URL = "${env.DATABASE_URL}"
  }

  stages {
    stage('Create virtual environment and install dependencies') {
      steps {
        sh '''
          python3 -m venv ${VENV_DIR}
          . ${VENV_DIR}/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Run Tests, collect logs and allure results') {
      steps {
        sh '''
          mkdir -p ${SHARED_DIR}/${ALLURE_RESULTS}
          mkdir -p ${SHARED_DIR}/${LOG_DIR}
          . ${VENV_DIR}/bin/activate
          pytest -v -s --alluredir=${SHARED_DIR}/${ALLURE_RESULTS} | tee ${SHARED_DIR}/${LOG_DIR}/test_output.log
        '''
      }
    }

    stage('Publish Allure Report') {
      steps {
        // Jenkins needs results inside workspace
        sh '''
          mkdir -p ${ALLURE_RESULTS}
          cp -r ${SHARED_DIR}/${ALLURE_RESULTS}/* ${ALLURE_RESULTS}/
        '''
        allure([
          includeProperties: false,
          jdk: '',
          reportBuildPolicy: 'ALWAYS',
          results: [[path: 'allure-results']]
        ])
      }
    }
  }

  post {
    always {
      // Also copy logs back to Jenkins workspace so they are archived
      sh '''
        mkdir -p logs
        cp -r ${SHARED_DIR}/${LOG_DIR}/* logs/ || true
      '''
      archiveArtifacts artifacts: 'logs/**, allure-results/**', allowEmptyArchive: true
    }
  }
}