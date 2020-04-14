module.exports = {
  base: '/ehr-functions/',
  title: 'EHR Functions',
  description: 'Documentation of the EHR Functions',
  head: [
    ['link', {rel: 'icon', href: '/favicon.ico'}] // TODO - This doesnt work
  ],
  themeConfig: {
    docsDir: 'docs',
    nav: [
      {text: 'Home', link: '/'},
      {text: 'Usage', link: '/usage/'},
      {text: 'Features', link: '/features/'},
      {text: 'Models', link: '/models/'},
    ],
    displayAllHeaders: true,
    sidebar: {
      '/usage/': [
        'installation',
        'assumptions',
        'examples',
      ],
      '/features/': [
        'codes',
        'demographics',
        'occurrence',
        'windows',
      ],
      '/models/':
        [
          {
            title: 'General',
            collapsable: false,
            children: [
              'train_model',
            ]
          },
          {
            title: 'Metrics',
            collapsable: false,
            children: [
              'metrics/base',
              'metrics/binary_classification',
              'metrics/roc_curve',
            ]
          },
          {
            title: 'Types',
            collapsable: false,
            children: [
              'types/base',
              'types/sklearn',
              'types/adaboost',
              'types/elastic_net',
              'types/linear_regression',
              'types/logistic_regression',
              'types/nn',
              'types/random_forest',
              'types/sgd',
              'types/svm',
            ]
          },
        ],
    }
  }
};