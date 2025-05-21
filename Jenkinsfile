pipeline {
  agent any

  environment {
    VENV_DIR = '.venv'
    ALLURE_RESULTS = 'allure-results'
    DATABASE_URL = "${env.DATABASE_URL}"
  }

    stage('Create virtual environment and install dependencies') {
      steps {
        dir('/workspace') {
          sh '''
            python3 -m venv ${VENV_DIR}
            . ${VENV_DIR}/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt
          '''
        }
      }
    }

    stage('Run Tests, collect logs and allure results') {
      steps {
        dir('/workspace') {
          sh '''
            . ${VENV_DIR}/bin/activate
            pytest -v -s --alluredir=/shared/${ALLURE_RESULTS}
          '''
        }
      }
    }

    stage('Publish Allure Report') {
      steps {
          dir('/workspace') {
            allure([
              includeProperties: false,
              jdk: '',
              reportBuildPolicy: 'ALWAYS',
              results: [[path: 'allure-results']]
            ])
          }
      }
    }
  }

  post {
    always {
        dir('/workspace') {
            archiveArtifacts artifacts: 'allure-results/**, logs/**', allowEmptyArchive: true
        }
    }
  }
}