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
    sidebar: {
      '/features/': [
        'demographics',
        // 'equation',
      ],
      '/models/': [
        //
      ],
    }
  }
};