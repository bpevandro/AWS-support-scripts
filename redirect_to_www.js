'use strict';
exports.handler = (event, context, callback) => {
    // Extract request from the CloudFront event
    var request = event.Records[0].cf.request;

    var params = '';
    if(('querystring' in request) && (request.querystring.length>0)) {
        params = '?'+request.querystring;
    }

    var miduri = request.uri.replace(/(\/[\w\-_]+)$/, '$1/');
    var newuri = "https://www.domain.com" + miduri + params;
    var str = request.headers.host[0].value;
    console.log(str)
    
    if (!str.startsWith("www")){
        const response = {
            status: '301',
            statusDescription: 'Permanently moved',
                headers: {
                location: [{
                    key: 'Location',
                    value: newuri
                    }]
                }
            };
        return callback(null, response);
    }
    return callback(null, request);
};
