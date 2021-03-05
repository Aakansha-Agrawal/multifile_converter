var file_input = document.getElementById("file_input");

var progress = document.getElementById("progress");
var progress_wrapper = document.getElementById("progress_wrapper");
var progress_status = document.getElementById("progress_status");

// var fpass = document.getElementById("fpass");
var from = document.getElementById("from");
var to = document.getElementById("to");

// var loading_btn = document.getElementById("loading_btn");
// var cancel_btn = document.getElementById("cancel_btn");

let count = 0;
var total_size = 0;

function input_filename(){
    file_input_label.innerHTML = input.files[0].name;
}

function upload(url) {
    if (!file_input.value) {
        console.log("No files Selected");
        return;
    }

    var data = new FormData();
    var request = new XMLHttpRequest();
    request.responseType = "json";

    // loading_btn.classList.remove("d-none");
    // cancel_btn.classList.remove("d-none");
    progress_wrapper.classList.remove("d-none");

    // input.disabled = true;
    // upload_btn
    all_files = file_input.files;

    for (let i = 0; i < all_files.length; ++i) {
        total_size += all_files[i].size;
        console.log(total_size);
    }

    data.set("file_input", all_files[count]);

    for (let i = 0; i < all_files.length; ++i) {
    
        var file = file_input.files[i];
        var filename = file.name;
        var filesize = file.size;
        // var filepass = fpass.value;
        var frompage  = from.value;
        var topage = to.value;

        document.cookie = `filesize=${filesize}`;
        // document.cookie = `filepass=${filepass}`;
        document.cookie = `frompage=${frompage}`;
        document.cookie = `topage=${topage}`;
        data.append("file", file);
        // console.log(filesize, from, to);

        request.upload.addEventListener("progress", function (e) {
            var loaded = e.loaded;
            var total = e.total;

            var percentage_complete = (loaded / total) * 100;
            progress.setAttribute("style", `width : ${Math.floor(percentage_complete)}%`);
            progress_status.innerText = `${Math.floor(percentage_complete)}% uploaded`;
            console.log(percentage_complete);
        })

        request.addEventListener("load", function (e) {
            if (request.status == 200) {
                console.log("success",frompage, topage);

                // ++count;
                // document.getElementById('file_input').innerHTML = count + ' files uploaded';
                // if (count < all_files.length) {
                //     data.set("file_input", all_files[count]);
                //     request.open('POST', url, true);
                //     request.send(data);
                // }
            }
            else {
                console.log("Error Upoading file");
            }
            reset();
        })

        request.addEventListener("error", function (e) {
            reset();
            console.log("Error uploading file");
        })

        // request.addEventListener("abort", function(e) {
        //     reset();
        //     console.log("Cancelled");
        // })

        // cancel_btn.addEventListener("click", function() {
        //     request.abort();
        // })

        request.open("POST", url, true);
        request.send(data);

        function reset() {
            file_input.value = null;
            all_files.value = null;
            // cancel_btn.classList.add("d-none");
            // loading_btn.classList.add("d-none");
            progress_wrapper.classList.add("d-none");
            progress.setAttribute("style", "width: 0%");
            // file_input_label.innerText = "Select File";
        }
    }
}